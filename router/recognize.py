from fastapi import APIRouter,File, UploadFile
from controller.recognize import face_recognize_c
router = APIRouter(
    prefix='/rgn',
    tags = ['face recognize']
)

@router.post("/")
def face_recognize(img: UploadFile = File(...)):
    """
    Face recognize
    """
    return face_recognize_c(img)