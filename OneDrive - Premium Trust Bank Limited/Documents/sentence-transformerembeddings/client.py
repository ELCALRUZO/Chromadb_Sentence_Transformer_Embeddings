import chromadb
from config import (
    COLLECTION_NAME,
    COLLECTION_METADATA,
    COLLECTION_CONFIGURATION
)

def get_chroma_client():
    return chromadb.Client()

def create_collection(client):
    return client.create_collection(
        name=COLLECTION_NAME,
        metadata=COLLECTION_METADATA,
        configuration=COLLECTION_CONFIGURATION
    )