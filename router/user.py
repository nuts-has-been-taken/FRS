from fastapi import APIRouter

router = APIRouter(
    prefix='/user',
    tags = ['user operation']
)

@router.post("/")
def upload_user():
    """
    Upload user information.
    """
    pass

@router.get("/{name}")
def get_user(name: str):
    """
    Get user information by name.
    """
    pass