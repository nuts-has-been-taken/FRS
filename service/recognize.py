from db.weaviate import weaviate_vector_search
from db.mongodb import mongo_get_user_by_id
from utils.deepface import get_face_vector
from utils.line import line_recog_unknown_user, line_recog_user
from fastapi import UploadFile

def face_recognize_s(img: UploadFile):

    # save img 
    with open(f"./user_photo/recognize/{img.filename}", "wb") as file_object:
        file_object.write(img.file.read())
    img_path = f"./user_photo/recognize/{img.filename}"

    # recognize
    vector = get_face_vector(img_path=img_path)
    res = weaviate_vector_search(near_vector={"vector": vector})
    if res["status"] == 0:
        print("沒有找到這個資料")
        line_recog_unknown_user()
        return {'msg': 'not found user', 'user': 'unknown'}
    
    # get user from mongodb
    user_id = res['msg']
    user_info = mongo_get_user_by_id(user_id=user_id)

    user = {
        "id": user_info['_id'],
        "name": user_info['name'],
        "phone": user_info['phone'],
        'identity': user_info['identity']
    }

    # line notify
    print(f"搜尋到此筆資料:{user}")
    line_recog_user(user)

    # del img
    # not implement

    return {'msg': 'found user', 'user': user}