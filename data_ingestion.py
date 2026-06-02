import pandas as pd
import numpy as np
import os

# Load all 10 CSV datasets
files = os.listdir("data/raw")
csv_files = [f for f in files if f.endswith(".csv")]

dataframes = {}

for file in csv_files:
    name = file.replace(".csv", "")
    df = pd.read_csv(f"data/raw/{file}")
    dataframes[name] = df
    print(f"\n{'='*50}")
    print(f"FILE: {file}")
    print(f"Shape: {df.shape}")
    print(f"\nDtypes:\n{df.dtypes}")
    print(f"\nFirst 2 rows:\n{df.head(2)}")

# Explore fund master
fm = dataframes["01_fund_master"]
print("\nUnique Fund Houses:", fm["fund_house"].unique())
print("Unique Categories:", fm["category"].unique())
print("Unique Sub-Categories:", fm["sub_category"].unique())
print("Unique Risk Grades:", fm["risk_category"].unique())

# Validate AMFI codes
nav = dataframes["02_nav_history"]
master_codes = set(fm["amfi_code"])
nav_codes = set(nav["amfi_code"])
missing = master_codes - nav_codes

print(f"\n--- AMFI VALIDATION ---")
print(f"Total codes in fund_master: {len(master_codes)}")
print(f"Matching codes: {len(master_codes & nav_codes)}")
print(f"Missing codes: {len(missing)}")

# Data quality summary
print("\n--- DATA QUALITY SUMMARY ---")
for name, df in dataframes.items():
    nulls = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()
    print(f"{name}: {df.shape[0]} rows | {nulls} nulls | {duplicates} duplicates")
