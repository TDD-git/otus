from fastapi import FastAPI
from starlette.status import HTTP_200_OK
import uvicorn

app = FastAPI()

@app.get(
    "/ping/",
    status_code=HTTP_200_OK
)
def ping_pong():
    return {"message": "pong"}

if __name__ == '__main__':
    uvicorn.run("main:app",
                reload=True,
                host="0.0.0.0",
                port=8000)