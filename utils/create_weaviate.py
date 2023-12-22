from db.weaviate import weaviate_create_db

def create_weaviate_schema():
    return weaviate_create_db()