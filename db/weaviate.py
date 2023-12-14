import weaviate
import os

W_API_KEY = os.getenv("WEAVIATE_API_KEY")
W_URL = os.getenv("WEAVIATE_URL")
URI = os.getenv("MONGODB_URL")


# Weaviate client instance
W_CLIENT = weaviate.Client(
    url=W_URL, auth_client_secret=weaviate.AuthApiKey(api_key=W_API_KEY)
)

def weaviate_create_user(user_params):
    try:
        vector = user_params['vector']
        name = user_params['name']
        with W_CLIENT.batch as batch:
            content = {
                "name":name,
            }
            uuid = batch.add_data_object(content, "Face", vector=vector)
        return {"status": 1, "msg": f"success, UID={uuid}", "uuid": uuid}
    except Exception as e:
        return {"status": 0, "msg": e}

def weaviate_get_user():
    pass

def weaviate_vector_search():
    pass