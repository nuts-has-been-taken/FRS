from db.weaviate import weaviate_vector_search
from db.mongodb import mongo_get_user
from utils.deepface import get_face_vector
from utils.line import line_recog_unknow_user, line_recog_user
from fastapi import UploadFile

def face_recognize_s(img: UploadFile):

    # save img 
    with open(f"./user_photo/recognize/{img.filename}", "wb") as file_object:
        file_object.write(img.file.read())
    img_path = f"./user_photo/recognize/{img.filename}"

    # recognize
    vector = get_face_vector(img_path=img_path)
    res = weaviate_vector_search(near_vector=vector)
    if res["status"] == 0:
        line_recog_unknow_user()
        return res
    
    # get user from mongodb
    user_id = res['msg']
    user = mongo_get_user(user_id=user_id)

    # line notify
    line_recog_user(user)

    # del img
    # not implement

    return {'msg': 'found user', 'user': user}