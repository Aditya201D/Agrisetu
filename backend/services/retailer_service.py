from database.queries import get_retailers_by_district_and_product

def search_retailers(district:str, product:str):
    return get_retailers_by_district_and_product(district, product)

def search_retailers_nearby(lat, lon, radius, product):
    return nearby_retailers(
        lat,
        lon,
        radius,
        product,
    )