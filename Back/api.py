from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path
from Back.routes import profRoute, coursRoute, salleRoute, promotionRoute, userRoute

app = FastAPI()

# Autoriser le front à faire des requêtes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"] ,
    allow_headers=["*"]
)

# Enregistrer tous les routers disponibles pour qu'ils apparaissent dans la doc OpenAPI (/docs)
app.include_router(profRoute.router)
app.include_router(coursRoute.router)
app.include_router(salleRoute.router)
app.include_router(promotionRoute.router)
app.include_router(userRoute.router)

BASE_DIR = Path(__file__).resolve().parent.parent
code_creation_prof = BASE_DIR / "Front" / "create_prof.html"
code_creation_user = BASE_DIR / "Front" / "create_user.html"

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}

@app.get("/prof")
def read_root():
    if code_creation_prof.exists():
        return FileResponse(str(code_creation_prof))
    return {"message": "Hello FastAPI"}

@app.get("/user")
def read_user():
    if code_creation_user.exists():
        return FileResponse(str(code_creation_user))
    return {"message": "Hello FastAPI"}