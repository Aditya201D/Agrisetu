from sqlalchemy import text
from database.connection import engine
from schemas.retailer import RetailerResult


def get_retailers_by_district_and_product(
    district: str,
    product: str,
):
    query = """
    SELECT
        r.retailer_id,
        r.agency_name,
        p.product_group AS product_name,
        i.quantity,
        r.latitude,
        r.longitude
    FROM retailers r
    JOIN inventory i
        ON r.retailer_id = i.retailer_id
    JOIN products p
        ON i.product_id = p.id
    WHERE r.district = :district
    """

    params = {
        "district": district,
    }

    if product != "All":
        query += """
        AND p.product_group = :product
        """
        params["product"] = product

    query += """
    ORDER BY i.quantity DESC
    LIMIT 10
    """

    with engine.connect() as conn:
        rows = conn.execute(text(query), params).mappings().all()

    return [
        RetailerResult.model_validate(row)
        for row in rows
    ]


def nearby_retailers(
    latitude: float,
    longitude: float,
    radius_km: float,
    product: str,
):
    query = """
    SELECT
        r.retailer_id,
        r.agency_name,
        p.product_group AS product_name,
        i.quantity,
        r.latitude,
        r.longitude,
        (
            6371 * acos(
                cos(radians(:lat))
                * cos(radians(r.latitude))
                * cos(radians(r.longitude) - radians(:lon))
                + sin(radians(:lat))
                * sin(radians(r.latitude))
            )
        ) AS distance

    FROM retailers r
    JOIN inventory i
        ON r.retailer_id = i.retailer_id
    JOIN products p
        ON i.product_id = p.id

    WHERE (
        6371 * acos(
            cos(radians(:lat))
            * cos(radians(r.latitude))
            * cos(radians(r.longitude) - radians(:lon))
            + sin(radians(:lat))
            * sin(radians(r.latitude))
        )
    ) <= :radius
    """

    params = {
        "lat": latitude,
        "lon": longitude,
        "radius": radius_km,
    }

    if product != "All":
        query += """
        AND p.product_group = :product
        """
        params["product"] = product

    query += """
    ORDER BY distance ASC
    LIMIT 10
    """

    with engine.connect() as conn:
        rows = conn.execute(text(query), params).mappings().all()

    return [
        RetailerResult.model_validate(row)
        for row in rows
    ]