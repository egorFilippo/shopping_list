from dotenv import load_dotenv
load_dotenv("../.env")

from fastapi import FastAPI
from api.handlers.routers import *


app = FastAPI()


@app.get("/")
def hi():
    return {"hello": "world"}


app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(group_router, prefix="/groups", tags=["Groups"])
app.include_router(group_member_router, prefix="/groups/members", tags=["Group Members"])
