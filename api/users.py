import os

from fastapi import FastAPI
from sqlalchemy import create_engine, text
from dotenv import load_dotenv




def get_users(engine):
    with engine.connect() as connection:
        result = connection.execute(
            text("select id, name from example_table")
        )

        return [
            {
                "id": row.id,
                "name": row.name
            }
            for row in result
        ]