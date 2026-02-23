from fastapi import FastAPI
from Back.routes import profRoute

app = FastAPI()

app.include_router(profRoute.router)

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}