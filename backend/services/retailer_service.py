from database.queries import get_retailers_by_district_and_product

def search_retailers_by_district(district:str, product:str):
    return get_retailers_by_district_and_product(district, product)