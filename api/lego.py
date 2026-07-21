import os

from fastapi import FastAPI
from sqlalchemy import create_engine, text
from dotenv import load_dotenv




def get_lego_proportions(engine):
    with engine.connect() as connection:
        result = connection.execute(
            text("select  name, year_proportion, theme_proportion, subtheme_proportion from public.mart_lego_piece_analysis")
        )

        return [
            {
                
                "name": row.name,
                "year_proportion": row.year_proportion,
                "theme_proportion": row.theme_proportion,
                "subtheme_proportion": row.subtheme_proportion,
            }
            for row in result
        ]