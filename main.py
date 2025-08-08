from contextlib import asynccontextmanager
from fastapi import FastAPI
import chromadb

chroma_client = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global chroma_client
    chroma_client = chromadb.Client()
    # Create or get a collection
    collection = chroma_client.get_or_create_collection(name="pull_agent_collection")
    print("ChromaDB initialized successfully")
    yield
    # chrome db doesnt need shutdown

app = FastAPI(lifespan=lifespan)

@app.get("/api/{subagent_role}")
async def get_role(subagent_role: str):
    return {"role_name": subagent_role, "message": f"Hello, {subagent_role}!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
