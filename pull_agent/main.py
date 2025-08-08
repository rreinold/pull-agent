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
        results = collection.get(ids=[subagent_role])
        
        if not results['documents'] or len(results['documents']) == 0:
            return {"error": f"Subagent role '{subagent_role}' not found"}
        
        return {
            "role_name": subagent_role,
            "markdown": results['documents'][0],
            "metadata": results['metadatas'][0] if results['metadatas'] else None
        }
    except Exception as e:
        return {"error": f"Failed to retrieve subagent: {str(e)}"}

@app.get("/status")
async def get_status(subagent_role: str):
    return {"status": "up!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
