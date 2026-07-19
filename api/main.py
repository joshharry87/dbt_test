import os

from fastapi import FastAPI
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

import users as u


load_dotenv()

DATABASE_URL = (
    f"postgresql://"
    f"{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:"
    f"{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

engine = create_engine(DATABASE_URL)

app = FastAPI(
    title="DBT + Postgres API"
)


@app.get("/")
def health():
    return {"status": "ok"}


@app.get("/users")
def get_users():
    
    return u.get_users(engine)
  