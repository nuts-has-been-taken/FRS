import os
import pymongo

# MongoDB client instance
URI = os.getenv("MONGODB_URL")
M_CLIENT = pymongo.MongoClient(URI)
DB = M_CLIENT["facedb"]
USER_COL = DB["user"]

# Create
def mongo_create_user(user_params):
    USER_COL.insert_one(user_params)
    return {"msg": f"success"}

# Get
def mongo_get_user_by_id(user_id):
    result = USER_COL.find({"_id": user_id})[0]
    return result

def mongo_get_user_by_name(name: str):
    if USER_COL.count_documents({"name": name})==0:
        return 0
    result = USER_COL.find({"name": name})
    return result[0]

# Update
def mongo_update_user_by_name(name: str, user_params:dict):
    update_info = {"$set": user_params}
    m_result = USER_COL.update_many({"name": name}, update_info)
    return m_result.modified_count

# Delete
def mongo_del_user_by_name(name: str):
    m_result = USER_COL.delete_many({"name":name})
    return m_result.deleted_count

# Delete All
def mongo_del_all():
    DB.drop_collection("user")
    return