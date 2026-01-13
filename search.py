def search_python_developers(collection):
    return collection.query(
        query_texts=["Python developer with web development experience"],
        n_results=3
    )

def search_leadership_roles(collection):
    return collection.query(
        query_texts=["team leader manager with experience"],
        n_results=3
    )

def filter_engineering(collection):
    return collection.get(where={"department": "Engineering"})

def filter_senior_staff(collection):
    return collection.get(where={"experience": {"$gte": 10}})

def combined_search(collection):
    return collection.query(
        query_texts=["senior Python developer full-stack"],
        n_results=5,
        where={
            "$and": [
                {"experience": {"$gte": 8}},
                {"location": {"$in": ["San Francisco", "New York", "Seattle"]}}
            ]
        }
    )
