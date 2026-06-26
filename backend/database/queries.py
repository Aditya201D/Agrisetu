from sqlalchemy import text
from database.connection import engine

def get_retailers_by_district_and_product(district:str, product:str):
    query = text("""
        SELECT
            r.id,
            r.name,
            r.address,
            r.phone,
            p.name AS product_name,
            s.quantity

        FROM retailers r

        JOIN stock s
            ON r.id = s.retailer_id

        JOIN products p
            ON p.id = s.product_id

        WHERE
            r.district = :district
            AND p.name = :product
            AND s.quantity > 0
    """)

    with engine.connect() as conn:
        result = conn.execute(
            query,
            {"district": district, "product": product}
        )
        rows = result.mappings().all()

        return rows