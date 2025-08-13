from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from fastapi.staticfiles import StaticFiles
import chromadb
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction
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
    # Configure embedding function to use the predownloaded model
    embedding_function = DefaultEmbeddingFunction()
    
    chroma_client = chromadb.Client()
    # Create or get a collection with the specific embedding function
    collection = chroma_client.get_or_create_collection(
        name="pull_agent_collection",
        embedding_function=embedding_function
    )
    
    # Load subagent configurations
    load_subagent_configs(collection)
    
    print("ChromaDB initialized successfully with predownloaded all-MiniLM-L6-v2 model")
    yield
    # chrome db doesnt need shutdown

app = FastAPI(lifespan=lifespan)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Mount static files from public directory
public_dir = Path(__file__).parent.parent / "public"
if public_dir.exists():
    app.mount("/", StaticFiles(directory=str(public_dir), html=True), name="static")

@app.get("/api/{subagent_role}", response_class=PlainTextResponse)
async def get_role(subagent_role: str):
    global chroma_client
    if not chroma_client:
        return "Error: ChromaDB not initialized"
    
    # If role_name is empty, default to senior-backend-engineer
    if not subagent_role or subagent_role.strip() == "":
        subagent_role = "senior-backend-engineer"
    
    try:
        collection = chroma_client.get_collection(name="pull_agent_collection")
        
        # First try exact ID lookup for performance
        exact_results = collection.get(ids=[subagent_role])
        if exact_results['documents'] and len(exact_results['documents']) > 0:
            return exact_results['documents'][0]
        
        # Fall back to semantic vector search
        search_results = collection.query(
            query_texts=[subagent_role],
            n_results=1
        )
        
        if not search_results['documents'] or len(search_results['documents']) == 0 or len(search_results['documents'][0]) == 0:
            return f"Error: No subagent found similar to '{subagent_role}'"
        
        # Return just the markdown content as plain text
        return search_results['documents'][0][0]
        
    except Exception as e:
        return f"Error: Failed to retrieve subagent: {str(e)}"

@app.get("/status")
async def get_status():
    return {"status": "up!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
