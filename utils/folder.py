import os

def create_photo_folder():
    if not os.path.exists("./user_photo"):
        os.mkdir("./user_photo")
        if not os.path.exists("./user_photo/create_user"):
            os.mkdir("./user_photo/create_user")
        if not os.path.exists("./user_photo/recognize"):
            os.mkdir("./user_photo/recognize")
    return