#!/usr/bin/env python3
"""
Script to download and cache ChromaDB embedding model during Docker build.
This ensures the model is available locally and doesn't need to be downloaded at runtime.
"""

import chromadb
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction
import tempfile
import os

def main():
    print("Downloading and caching ChromaDB embedding model...")
    
    # Create a temporary client and collection to trigger model download
    client = chromadb.Client()
    embedding_function = DefaultEmbeddingFunction()
    
    # Create collection with embedding function (this triggers model download)
    collection = client.get_or_create_collection(
        name="model_cache_temp", 
        embedding_function=embedding_function
    )
    
    # Add a dummy document to ensure embedding function is fully initialized
    collection.add(
        documents=["This is a test document to initialize the embedding model."],
        ids=["test_1"]
    )
    
    print("Model successfully downloaded and cached!")
    
    # Clean up temporary collection
    client.delete_collection("model_cache_temp")
    print("Temporary collection cleaned up.")

if __name__ == "__main__":
    main()