import glob
import os
import pandas as pd

folder = r"C:\Users\viktoriia.vitko\Projects\OECD_CRS\CRS_data"
files = glob.glob(os.path.join(folder, "CRS*.txt"))

dfs = []

for file in files:
    print("Reading:", os.path.basename(file))

    chunk_iter = pd.read_csv(
        file,
        sep="|",
        quotechar='"',
        engine="python",
        chunksize=100_000,
    )

    for chunk in chunk_iter:
        # Make sure column exists
        if "RecipientName" not in chunk.columns:
            continue

        # Convert to string before using .str
        mask = (
            chunk["RecipientName"]
            .astype(str)
            .str.strip()
            .str.lower()
            == "south africa"
        )

        filtered = chunk[mask]

        if not filtered.empty:
            dfs.append(filtered)

# 🔒 Safe concatenation
if dfs:
    full_df = pd.concat(dfs, ignore_index=True)
    output = r"C:\Users\viktoriia.vitko\Projects\OECD_CRS\CRS_south_africa.csv"
    full_df.to_csv(output, index=False)
    print("✅ Combined dataset saved!")
    print("Rows:", len(full_df))
else:
    print("⚠️ No records found.")