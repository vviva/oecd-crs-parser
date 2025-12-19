import requests
import pandas as pd

# ====== 1. Set your API URL ======
url = "https://sxs-boost-oecd.redpelicans.com/boost-disseminate/v2/sdmx/data/OECD.DCD.FSD,DSD_CRS@DF_CRS,1.4/DAC.SOM.1000.14+60+100._T._T.C+D.Q._T..?startPeriod=2020&dimensionAtObservation=AllDimensions"

# ====== 2. Fetch the data ======
r = requests.get(url)
r.raise_for_status()  # check if the request worked
data = r.json()        # parse JSON

# ====== 3. Read dimension info ======
dims = data["data"]["structure"]["dimensions"]["observation"]
codes = [d["name"] for d in dims]

# ====== 4. Flatten observations ======
obs = data["data"]["dataSets"][0]["observations"]
rows = []
for key, val in obs.items():
    indices = [int(i) for i in key.split(":")]
    row = {}
    for i, idx in enumerate(indices):
        dim = dims[i]
        if "values" in dim:
            # Classic SDMX dimension
            row[codes[i]] = dim["values"][idx]["name"]
        elif "categories" in dim:
            # Some dimensions use "categories"
            row[codes[i]] = dim["categories"][idx]["name"]
        else:
            # Fallback: use the dimension id
            row[codes[i]] = dim.get("name", f"dim{i}")
    # Add the actual observation value
    row["value"] = val[0]
    rows.append(row)

# ====== 5. Convert to DataFrame ======
df = pd.DataFrame(rows)

# ====== 6. Save to CSV ======
df.to_csv("crs_data.csv", index=False)

with open(r"C:\Users\viktoriia.vitko\OECD_CRS\CRS_data", "r", encoding="utf-8") as f:
    for i in range(10):
        print(f.readline().strip())