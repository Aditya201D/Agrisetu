import os
from dotenv import load_dotenv
load_dotenv()

db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

from sqlalchemy import create_engine

DATABASE_URL = (
    f"mysql+pymysql://{db_username}:{db_password}@localhost/{db_name}"
)

engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True)