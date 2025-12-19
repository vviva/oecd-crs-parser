import glob
import os
import pandas as pd

folder = r"C:\Users\viktoriia.vitko\Projects\OECD_CRS"
file_path = os.path.join(folder, "CRS 2024 data.txt")

dfs = []

df = pd.read_csv(
    file_path,
    sep="|",
    quotechar='"',
    engine="python",
)

# 🔒 Safe concatenation
output = r"C:\Users\viktoriia.vitko\Projects\OECD_CRS\CRS_2024.csv"
df.to_csv(output, index=False)

print("✅ CSV file created successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))