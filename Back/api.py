from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
from Back.routes import profRoute, coursRoute, salleRoute, promotionRoute

app = FastAPI()

# Enregistrer tous les routers disponibles pour qu'ils apparaissent dans la doc OpenAPI (/docs)
app.include_router(profRoute.router)
app.include_router(coursRoute.router)
app.include_router(salleRoute.router)
app.include_router(promotionRoute.router)

BASE_DIR = Path(__file__).resolve().parent.parent
code_creation_prof = BASE_DIR / "Front" / "create_prof.html"

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}

@app.get("/prof")
def read_root():
    if code_creation_prof.exists():
        return FileResponse(str(code_creation_prof))
    return {"message": "Hello FastAPI"}