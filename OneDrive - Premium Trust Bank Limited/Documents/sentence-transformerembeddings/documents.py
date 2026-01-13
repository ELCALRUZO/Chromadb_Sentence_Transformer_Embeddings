def build_employee_document(employee: dict) -> str:
    return (
        f"{employee['role']} with {employee['experience']} years of experience "
        f"in {employee['department']}. Skills: {employee['skills']}. "
        f"Located in {employee['location']}. "
        f"Employment type: {employee['employment_type']}."
    )
