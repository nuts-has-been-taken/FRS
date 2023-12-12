from fastapi import APIRouter

router = APIRouter(
    prefix='/rgn',
    tags = ['face recognize']
)

@router.post("/")
def face_recognize():
    """
    Face recognize
    """
    pass