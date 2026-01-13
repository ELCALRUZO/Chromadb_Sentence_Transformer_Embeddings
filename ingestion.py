from documents import build_employee_document

def ingest_employees(collection, employees):
    collection.add(
        ids=[e["id"] for e in employees],
        documents=[build_employee_document(e) for e in employees],
        metadatas=[{
            "name": e["name"],
            "department": e["department"],
            "role": e["role"],
            "experience": e["experience"],
            "location": e["location"],
            "employment_type": e["employment_type"]
        } for e in employees]
    )
