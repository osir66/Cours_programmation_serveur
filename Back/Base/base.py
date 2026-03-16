from sqlmodel import create_engine, SQLModel
from fastapi import FastAPI
from contextlib import asynccontextmanager
from classe_bd import Prof, Promotion, User, Salle, Cours


db_file_name = "database.db"
db_url = f"sqlite:///{db_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(db_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)