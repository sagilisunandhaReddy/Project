import pandas as pd
import os

folder = "data/raw"

all_nav = []
fund_master = []

for file in os.listdir(folder):

    if file.endswith("_nav.csv"):

        df = pd.read_csv(os.path.join(folder, file))

        # Add to combined NAV history
        all_nav.append(df)

        # Create basic fund master entry
        fund_master.append({
            "file_name": file,
            "rows": len(df),
            "start_date": df["date"].iloc[-1],
            "latest_date": df["date"].iloc[0]
        })

# Combined NAV history
nav_history = pd.concat(all_nav, ignore_index=True)
nav_history.to_csv(
    "data/raw/nav_history.csv",
    index=False
)

# Fund master
fund_master_df = pd.DataFrame(fund_master)
fund_master_df.to_csv(
    "data/raw/fund_master.csv",
    index=False
)

print("Created:")
print("data/raw/nav_history.csv")
print("data/raw/fund_master.csv")