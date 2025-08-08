from contextlib import asynccontextmanager
from fastapi import FastAPI
import chromadb
import os
from pathlib import Path

chroma_client = None

def load_subagent_configs(collection):
    """Load subagent markdown files into ChromaDB collection"""
    subagents_dir = Path(__file__).parent.parent / "subagents"
    if subagents_dir.exists():
        ids = []
        documents = []
        metadatas = []
        
        for md_file in subagents_dir.glob("*.md"):
            role_name = md_file.stem  # filename without extension
            content = md_file.read_text(encoding="utf-8")
            
            ids.append(role_name)
            documents.append(content)
            metadatas.append({"filename": md_file.name, "role": role_name})
        
        if ids:
            collection.add(ids=ids, documents=documents, metadatas=metadatas)
            print(f"Loaded {len(ids)} subagent configurations into ChromaDB")
        return len(ids)
    return 0

@asynccontextmanager
async def lifespan(app: FastAPI):
    global chroma_client
    chroma_client = chromadb.Client()
    # Create or get a collection
    collection = chroma_client.get_or_create_collection(name="pull_agent_collection")
    
    # Load subagent configurations
    load_subagent_configs(collection)
    
    print("ChromaDB initialized successfully")
    yield
    # chrome db doesnt need shutdown

app = FastAPI(lifespan=lifespan)

@app.get("/api/{subagent_role}")
async def get_role(subagent_role: str):
    global chroma_client
    if not chroma_client:
        return {"error": "ChromaDB not initialized"}
    
    try:
        collection = chroma_client.get_collection(name="pull_agent_collection")
        
        # First try exact ID lookup for performance
        exact_results = collection.get(ids=[subagent_role])
        if exact_results['documents'] and len(exact_results['documents']) > 0:
            return {
                "role_name": subagent_role,
                "markdown": exact_results['documents'][0],
                "metadata": exact_results['metadatas'][0] if exact_results['metadatas'] else None,
                "match_type": "exact"
            }
        
        # Fall back to semantic vector search
        search_results = collection.query(
            query_texts=[subagent_role],
            n_results=1
        )
        
        if not search_results['documents'] or len(search_results['documents']) == 0 or len(search_results['documents'][0]) == 0:
            return {"error": f"No subagent found similar to '{subagent_role}'"}
        
        # Get the best match
        best_match_id = search_results['ids'][0][0]
        best_match_document = search_results['documents'][0][0]
        best_match_metadata = search_results['metadatas'][0][0] if search_results['metadatas'] and search_results['metadatas'][0] else None
        similarity_score = search_results['distances'][0][0] if search_results.get('distances') else None
        
        return {
            "role_name": best_match_id,
            "markdown": best_match_document,
            "metadata": best_match_metadata,
            "match_type": "semantic",
            "similarity_score": similarity_score,
            "query": subagent_role
        }
    except Exception as e:
        return {"error": f"Failed to retrieve subagent: {str(e)}"}

@app.get("/status")
async def get_status(subagent_role: str):
    return {"status": "up!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
