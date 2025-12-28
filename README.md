# PSG Stats Export (FBref → Excel/CSV)

This project is a small Python utility that **scrapes Paris Saint-Germain (PSG) team stats from FBref** (season 2024–2025, all competitions) and exports the first table found to an **Excel file**.

The script uses `pandas.read_html()` to fetch tables from the FBref page, prints the detected columns, flattens MultiIndex columns when needed, then exports the data to `psg_stats_2024_2025.xlsx`. :contentReference[oaicite:0]{index=0}

---

## Features

- Fetches FBref tables directly from the PSG stats page
- Displays available table columns (useful to choose the right table index)
- Handles MultiIndex headers by flattening column names
- Exports results to Excel (`.xlsx`)

---

## Repository contents

- `psg_export.py` — main script :contentReference[oaicite:1]{index=1}
- `psg_stats_2024_2025.xlsx` — generated export (Excel)
- `psg_stats_2024_2025.csv` — optional/alternative export (CSV, easier to preview on GitHub)

> Note: GitHub usually does **not preview `.xlsx` files** nicely. If you want data to be readable directly in the repo, prefer a `.csv`.

---

## Requirements

- Python 3.9+
- pandas
- HTML parser for `read_html()` (usually `lxml` or `html5lib`)
- Excel writer for `.xlsx` export (`openpyxl`)

Install dependencies:

```bash
pip install pandas lxml openpyxl
