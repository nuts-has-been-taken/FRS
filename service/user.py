from fastapi import UploadFile
from db.weaviate import weaviate_create_user, weaviate_del_user_by_name, weaviate_del_all, weaviate_create_db
from db.mongodb import mongo_create_user, mongo_del_user_by_name, mongo_update_user_by_name, mongo_get_user_by_name, mongo_del_all
from utils.line import line_create_user
from utils.deepface import get_face_vector

# Get
def get_user_by_name_s(name:str):
    res = mongo_get_user_by_name(name)
    res.pop('vector')
    return res

# Create
def create_user_s(imgs: list[UploadFile], user_params):
    # save img and put params to db
    
    try:
        for img in imgs:
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
            
            line_create_user(name=user_params['name'], uuid=uuid)
            
    except Exception as e:
        # del user in weaviate & mongodb
        print(e)
        return {"msg": e}
        
    return {"msg": f"create success"}

# Update
def update_user_info_s(user_params:dict):
    try:
        name = user_params['name']
        user_old_info = get_user_by_name_s(name)

        # set params
        phone = user_params['phone'] if user_params['phone'] else user_old_info['phone']
        identity = user_params['identity'] if user_params['identity'] else user_old_info['identity']
        user_new_info = {
            "phone":phone,
            "identity":identity,
        }
        
        # update new info
        mongo_update_user_by_name(name, user_new_info)
        return {"msg": f"update success"}
    except Exception as e:
        return {"msg": f"Error: {e}"}

# Delete
def del_user_s(name: str):
    try:
        # delete mongodb data
        mongo_del_user_by_name(name)
        # delete weaviate data
        weaviate_del_user_by_name(name)
        return {"msg": f"delete success"}
    except Exception as e:
        return {"msg": f"Error: {e}"}

def del_all_user_s():
    try:
        # delete mongodb data
        mongo_del_all()
        # delete weaviate data
        weaviate_del_all()
        # recreate the weaviate schema
        weaviate_create_db()
        return {"msg": f"delete success"}
    except Exception as e:
        return {"msg": f"Error: {e}"}
