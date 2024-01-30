from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import users

app = FastAPI()
app.include_router(users.router, tags=['users'])
app.mount("/static", StaticFiles(directory="static"), name="static")
