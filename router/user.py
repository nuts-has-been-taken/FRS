from fastapi import APIRouter,File, UploadFile, Form
from controller.user import create_user_c, update_user_info_c, del_user_c, get_user_c, del_all_user_c

router = APIRouter(
    prefix='/user',
    tags = ['user operation']
)

# Create
@router.post("/")
def upload_user(
    name: str = Form(...),
    phone: str = Form(...),
    identity: str = Form(...),
    imgs: list[UploadFile] = File(...),
):
    """
    Upload user information.
    """
    return create_user_c(imgs=imgs, name=name, phone=phone, identity=identity)

# Get
@router.get("/{name}")
def get_user(name: str):
    """
    Get user information by name.
    """
    return get_user_c(name)

# Update
@router.post("/{name}")
def update_user(
    name: str,
    phone: str = Form(None, required=False),
    identity: str = Form(None, required=False),
    ):
    """
    Update user info
    """
    return update_user_info_c(name, phone, identity)

# Delete
@router.delete("/{name}")
def del_user(
    name: str
    ):
    """
    Delete user
    """
    return del_user_c(name)

@router.delete("/")
def del_all_user():
    """
    Delete all user
    """
    return del_all_user_c()