import pandas as pd
from sqlalchemy import create_engine
import os

os.makedirs("data/db", exist_ok=True)

engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

fund_master = pd.read_csv(
    "data/raw/fund_master.csv"
)

nav_history = pd.read_csv(
    "data/raw/nav_history.csv"
)

fund_master.to_sql(
    "fund_master",
    engine,
    if_exists="replace",
    index=False
)

nav_history.to_sql(
    "nav_history",
    engine,
    if_exists="replace",
    index=False
)

print("Database created successfully!")