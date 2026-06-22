from sqlalchemy import create_engine

DATABASE_URL = (
    "mysql+pymysql://user:thakur201@localhost/agrisetu"
)

engine = create_engine(DATABASE_URL, echo=True)