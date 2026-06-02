import pandas as pd

df = pd.read_csv("data/raw/fund_master.csv")

print("="*50)
print("Fund Master Overview")
print("="*50)

print("\nColumns:")
print(df.columns)

for col in df.columns:
    print(f"\nUnique values in {col}:")
    print(df[col].unique())
    