This tool converts OECD CRS dotStat .txt files into CSV format and optionally filters the data by recipient country.

1. What this tool does

Reads OECD CRS dotStat .txt files

Converts them into a standard .csv file

Optionally filters data for a specific recipient country (e.g. Somalia, Kenya, etc)

2. What you need before you start

2.1 Install Python (only once)

Go to: https://www.python.org/downloads/

Click Download Python 3

Run the installer

IMPORTANT: Check the box
☑ Add Python to PATH

Click Install Now

To check installation:

Open Command Prompt

Type:

python --version


You should see something like Python 3.12.x

3. Download this tool

Click the green Code button on this page

Choose Download ZIP

Extract the ZIP file to a folder, for example:

C:\CRS_parser

Your folder should now contain:

CRS_parser\
│
├── crs_parser.py

├── requirements.txt

└── README.md

4. Prepare your CRS data

Download OECD CRS dotStat data

Extract the .zip file

Place all .txt files into one folder, inside your CRS_parser directory. For example:

C:\CRS_parser\CRS_data

5. Install required Python packages

Open Command Prompt

Navigate to the folder where you extracted the tool:

cd C:\CRS_parser

Run:

pip install -r requirements.txt

This only needs to be done once.

6. Convert CRS files to CSV
6.1 Convert ALL data (no filtering)
python crs_parser.py --input CRS_data --output full_crs.csv

This creates:

full_crs.csv

6.2 Convert data for ONE recipient country

Example: Somalia

python crs_parser.py --input CRS_data --recipient Somalia --output somalia.csv

7. Where is my output file?

The output CSV file is saved:

In the folder where you ran the command, unless

You specify a full path in --output

Example:

--output C:\CRS_output\somalia.csv

8. Common problems and solutions
“python is not recognized”

Python is not installed or

“Add Python to PATH” was not selected
→ Reinstall Python and check the box

“No .txt files found”

Check that:

CRS files are .txt

They are inside the folder you passed to --input

Output file is empty

Check spelling of the recipient country

Use English country names (e.g. Somalia, not SOM)

9. Notes on CRS data

CRS files are large; processing may take several minutes

The tool reads data in chunks to avoid memory issues

Country name matching is case-insensitive

10. Example folder setup (recommended)
C:\
│
├── CRS_parser\

│   ├── crs_parser.py

│   ├── requirements.txt

│   └── README.md 

    └──CRS_data\
│       ├── CRS2022.txt
│       ├── CRS2023.txt
│       └── CRS2024.txt

    └── kenya.csv

11. Support

If you encounter issues:

Double-check file paths

Ensure Python is installed correctly

Review error messages carefully
