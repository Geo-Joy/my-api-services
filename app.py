from fastapi import FastAPI

api = FastAPI()


@api.get("/")
async def root():
    return {"message": "Hello World! Again 2"}


@api.get("/health")
async def health():
    return {"message": "pass"}
