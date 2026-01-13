from client import get_chroma_client, create_collection
from data import EMPLOYEES
from ingestion import ingest_employees
from search import (
    search_python_developers,
    search_leadership_roles,
    filter_engineering,
    filter_senior_staff,
    combined_search
)

def main():
    client = get_chroma_client()
    collection = create_collection(client)

    print(f"Collection created: {collection.name}")

    ingest_employees(collection, EMPLOYEES)

    print("Python Developers:", search_python_developers(collection))
    print("Leadership Roles:", search_leadership_roles(collection))
    print("Engineering Staff:", filter_engineering(collection))
    print("Senior Staff:", filter_senior_staff(collection))
    print("Combined Search:", combined_search(collection))

if __name__ == "__main__":
    main()
