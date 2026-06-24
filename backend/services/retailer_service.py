from database.queries import get_retailers_by_district_and_product

def search_retailers(district:str, product:str):
    return get_retailers_by_district_and_product(district, product)