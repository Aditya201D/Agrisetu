from sqlalchemy import text
from database.connection import engine


def get_retailers_by_district_and_product(
    district: str,
    product: str,
):
    query = text("""
        SELECT
            r.retailer_id, r.agency_name, r.latitude, r.longitude, p.product_group AS product_name, i.quantity
        FROM inventory i
        JOIN retailers r
            ON i.retailer_id = r.retailer_id
        JOIN products p
            ON i.product_id = p.id
        WHERE
            r.district_name = :district
            AND
            p.product_group = :product
            AND
            i.quantity > 0
        ORDER BY
            i.quantity DESC
        LIMIT 10
    """)

    with engine.connect() as conn:
        result = conn.execute(
            query,
            {
                "district": district,
                "product": product,
            },
        )

        return result.mappings().all()