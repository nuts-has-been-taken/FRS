from fastapi import UploadFile
from db.weaviate import weaviate_create_user
from db.mongodb import mongo_create_user
from utils.line import line_create_user
from utils.deepface import get_face_vector

def get_user_s():
    pass

def create_user_s(img: UploadFile, user_params):
    # save img and put params to db
    try:
        # save img
        with open(f"./user_photo/create_user/{img.filename}", "wb") as file_object:
            file_object.write(img.file.read())
        img_path = f"./user_photo/create_user/{img.filename}"

        # use deepface
        vector = get_face_vector(img_path=img_path)
        user_params['vector'] = vector
        w_res = weaviate_create_user(user_params=user_params)
        uuid = w_res['uuid']
        user_params['_id'] = uuid
        m_res = mongo_create_user(user_params=user_params)
        
        if m_res["status"] == 1 and w_res["status"] == 1:
            line_create_user(name=user_params['name'], uuid=uuid)
            return {"msg": f"create success, user id is {uuid}"}
        else:
            return {"msg": f"Create user fail, err msg: Weaviate:\n{w_res['msg']}\nMongoDB:\n{m_res['msg']}"}
    except Exception as e:
        # del user in weaviate & mongodb
        return {"msg": e}