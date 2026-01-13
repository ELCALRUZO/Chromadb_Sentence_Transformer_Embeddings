from chromadb.utils import embedding_functions

EMBEDDING_FUNCTION = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

COLLECTION_NAME = "employee_collection"

COLLECTION_METADATA = {
    "description": "A collection for storing employee data"
}

COLLECTION_CONFIGURATION = {
    "hnsw": {"space": "cosine"},
    "embedding_function": EMBEDDING_FUNCTION
}
