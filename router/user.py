from fastapi import APIRouter,File, UploadFile, Form
from controller.user import create_user_c

router = APIRouter(
    prefix='/user',
    tags = ['user operation']
)

@router.post("/")
def upload_user(
    name: str = Form(...),
    phone: str = Form(...),
    img: UploadFile = File(...),
):
    """
    Upload user information.
    """
    return create_user_c(img=img, name=name, phone=phone)

@router.get("/{name}")
def get_user(name: str):
    """
    Get user information by name.
    """
    pass