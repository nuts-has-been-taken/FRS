from deepface import DeepFace

def get_face_vector(img_path):
    return DeepFace.represent(img_path=img_path, model_name="ArcFace")[0]["embedding"]