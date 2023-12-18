from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from utils.folder import create_photo_folder
import router.recognize
import router.user
import uvicorn

app = FastAPI()
app.include_router(router.user.router)
app.include_router(router.recognize.router)

@app.get("/")
def read_root():
    return {"message": "This is facial reconition server from NYCU CCSA class project."}

if __name__ == "__main__":
    create_photo_folder()
    uvicorn.run(app, host="0.0.0.0", port=8100)