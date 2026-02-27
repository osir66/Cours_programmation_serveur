from fastapi import FastAPI
from Back.routes import profRoute, coursRoute, salleRoute, promotionRoute

app = FastAPI()

# Enregistrer tous les routers disponibles pour qu'ils apparaissent dans la doc OpenAPI (/docs)
app.include_router(profRoute.router)
app.include_router(coursRoute.router)
app.include_router(salleRoute.router)
app.include_router(promotionRoute.router)

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}