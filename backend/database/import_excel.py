import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()

db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+pymysql://{db_username}:{db_password}@localhost/{db_name}"

engine = create_engine(DATABASE_URL)

EXCEL_FILE = "/home/aditya201d/agrisetu/backend/Retailer Stock Sample data(1).xlsx"

df = pd.read_excel(EXCEL_FILE)

print(f"Rows in dataset: {len(df)}")

retailers = (
    df[
        [
            "Retailer Id",
            "Agency Name",
            "District Name",
            "State Name",
            "Latitude",
            "Longitude",
        ]
    ]
    .drop_duplicates(subset="Retailer Id")
)

retailers.columns = [
    "retailer_id",
    "agency_name",
    "district_name",
    "state_name",
    "latitude",
    "longitude",
]

retailers.to_sql(
    "retailers",
    engine,
    if_exists="append",
    index=False,
)

print(f"Inserted {len(retailers)} retailers.")


products = (
    df[["Product Group Name"]]
    .drop_duplicates()
    .rename(columns={
        "Product Group Name": "product_group"
    })
)

products.to_sql(
    "products",
    engine,
    if_exists="append",
    index=False,
)

print(f"Inserted {len(products)} products.")

product_lookup = pd.read_sql(
    "SELECT id, product_group FROM products",
    engine
)

product_map = dict(
    zip(
        product_lookup.product_group,
        product_lookup.id,
    )
)

inventory = pd.DataFrame()

inventory["retailer_id"] = df["Retailer Id"]

inventory["product_id"] = (
    df["Product Group Name"]
    .map(product_map)
)

inventory["company_name"] = df["Company Name"]

inventory["plant_name"] = df["Plant Name"]

inventory["quantity"] = df["Quantity(MT.)"]

inventory.to_sql(
    "inventory",
    engine,
    if_exists="append",
    index=False,
)

print(f"Inserted {len(inventory)} inventory rows.")