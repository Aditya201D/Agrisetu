from sqlalchemy import text
from database.connection import engine

def get_retailers_by_district(district:str):
    query = text("""
        SELECT id, name, address, phone
                 FROM retailers
                 WHERE district = :district
    """)

    with engine.connect() as conn:
        result = conn.execute(
            query,
            {"district": district}
        )
        rows = result.fetchall()

        return rows