import weaviate
import os

W_API_KEY = os.getenv("WEAVIATE_API_KEY")
W_URL = os.getenv("WEAVIATE_URL")
URI = os.getenv("MONGODB_URL")


# Weaviate client instance
W_CLIENT = weaviate.Client(
    url=W_URL, auth_client_secret=weaviate.AuthApiKey(api_key=W_API_KEY)
)

# Create weaviate schema
def weaviate_create_db():
    try:
        class_obj = {
            'class': 'Face',
            'properties': [
                {
                    'name': 'name',
                    'dataType': ['text'],
                },
            ],
        }
        W_CLIENT.schema.create_class(class_obj)
    except Exception as e:
        print("Loading data from exists weaviate Face collection")
    return

# Create
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

# Get
def weaviate_get_user():
    pass

def weaviate_vector_search(near_vector:dict):
    """
    example: 
    near_vector: {
        "vector" : vector(list),
    }
    """
    result = (
        W_CLIENT.query.get("Face", ["name"])
        .with_near_vector(near_vector)
        .with_limit(1)
        .with_additional(['id', 'certainty'])
        .do()
    )
    if result["data"]["Get"]["Face"][0]["_additional"]["certainty"] > 0.6:
        return {
            "status": 1,
            "msg": result["data"]["Get"]["Face"][0]["_additional"]["id"],
        }
    else:
        return {"status": 0, "msg": "unknown user"}

# Update
def weaviate_update_user_vector(uuid: str, vector):
    pass

# Delete
def weaviate_del_user_by_id(uuid):
    w_result = W_CLIENT.batch.delete_objects(
        class_name="Face",
        where={"operator": "Equal", "path": ["uuid"], "valueText": uuid},
        output="verbose",
        dry_run=False,
    )
    return

def weaviate_del_user_by_name(name):
    w_result = W_CLIENT.batch.delete_objects(
        class_name="Face",
        where={"operator": "Equal", "path": ["name"], "valueText": name},
        output="verbose",
        dry_run=False,
    )
    return

# Delete All
def weaviate_del_all():
    W_CLIENT.schema.delete_class(class_name="Face")
    return