from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.folder import create_photo_folder
from utils.create_weaviate import create_weaviate_schema
import router.recognize
import router.user
import uvicorn

app = FastAPI()
app.include_router(router.user.router)
app.include_router(router.recognize.router)

# Access-Control-Allow-Origin
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "This is facial reconition server from NYCU CCSA class project."}

def set_util():
    create_photo_folder()
    create_weaviate_schema()

if __name__ == "__main__":
    set_util()
    uvicorn.run(app, host="0.0.0.0", port=8100)