import requests
import pandas as pd
import os

# Create raw data folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

schemes = {
    125497: "hdfc_top100",
    119551: "sbi_bluechip",
    120503: "icici_bluechip",
    118632: "nippon_largecap",
    119092: "axis_bluechip",
    120841: "kotak_bluechip"
}

for scheme_code, filename in schemes.items():

    print(f"Downloading {filename}...")

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        nav_df.to_csv(
            f"data/raw/{filename}_nav.csv",
            index=False
        )

        print(f"Saved {filename}_nav.csv")

    else:
        print(f"Failed for {scheme_code}")