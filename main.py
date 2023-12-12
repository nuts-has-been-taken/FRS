from fastapi import FastAPI
import router.recognize
import router.user
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "This is facial reconition server from NYCU CCSA class project."}

app.include_router(router.user.router)
app.include_router(router.recognize.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8100)