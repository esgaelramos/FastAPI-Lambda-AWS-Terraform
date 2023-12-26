import os
import uvicorn
from fastapi import FastAPI
from mangum import Mangum


app = FastAPI()


@app.get("/")
def index():
    return "Hello, from FastAPI-Lambda-AWS-Terraform"


handler = Mangum(app, lifespan="off")

if __name__ == "__main__":
    uvicorn_app = f"{os.path.basename(__file__).removesuffix('.py')}:app"
    uvicorn.run(uvicorn_app, host="0.0.0.0", port=8000, reload=True)