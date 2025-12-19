import argparse
import glob
import os
import pandas as pd

def parse_crs(input_dir, recipient, output_file):
    files = glob.glob(os.path.join(input_dir, "CRS*.txt"))

    if not files:
        raise FileNotFoundError(f"No .txt files found in {input_dir}")

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

            # If no recipient filter → keep entire chunk
            if not recipient:
                dfs.append(chunk)
                continue

            # Make sure column exists
            if "RecipientName" not in chunk.columns:
                continue

        # Convert to string before using .str
            mask = (
                chunk["RecipientName"]
                .astype(str)
                .str.strip()
                .str.lower()
                == recipient.lower()
            )

            filtered = chunk[mask]

            if not filtered.empty:
                dfs.append(filtered)

# 🔒 Safe concatenation
    if dfs:
        full_df = pd.concat(dfs, ignore_index=True)
        full_df.to_csv(output_file, index=False)
        print("✅ Combined dataset saved!")
        print("Rows:", len(full_df))
    else:
        print("⚠️ No records found.")


def main():
    parser = argparse.ArgumentParser(
        description="Parse OECD CRS DOCSTAT files and filter by recipient country"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Folder containing CRS .txt files"
    )

    parser.add_argument(
        "--recipient",
        required=False,
        default=None,
        help="Recipient country name (e.g. Kenya, Somalia)"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Path to output CSV file"
    )

    args = parser.parse_args()

    parse_crs(args.input, args.recipient, args.output)


if __name__ == "__main__":
    main()