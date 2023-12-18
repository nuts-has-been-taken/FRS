import os
import pymongo

# MongoDB client instance
URI = os.getenv("MONGODB_URL")
M_CLIENT = pymongo.MongoClient(URI)
DB = M_CLIENT["facedb"]
USER_COL = DB["user"]

def mongo_create_user(user_params):
    try:
        USER_COL.insert_one(user_params)
        return {"status": 1, "msg": f"success"}
    except Exception as e:
        return {"status": 0, "msg": e}

def mongo_get_user(user_id):
    try:
        result = USER_COL.find({"_id": user_id})[0]
        return {"status": 1, "msg": result}
    except Exception as e:
        return {"status": 0, "msg": e}