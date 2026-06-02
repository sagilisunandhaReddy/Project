import pandas as pd

master = pd.read_csv("data/raw/fund_master.csv")
history = pd.read_csv("data/raw/nav_history.csv")

print("Fund Master Shape:", master.shape)
print("NAV History Shape:", history.shape)

if "scheme_code" in master.columns and "scheme_code" in history.columns:

    master_codes = set(master["scheme_code"])
    history_codes = set(history["scheme_code"])

    missing = master_codes - history_codes

    print("\nMissing Codes:")
    print(missing)

    if len(missing) == 0:
        print("\nAll AMFI codes validated successfully.")
else:
    print("\nscheme_code column not found.")