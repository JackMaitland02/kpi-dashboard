# KPI Dashboard (Python)
A lightweight KPI dashboard built in Python that reads monthly financial data from a CSV, calculates core performance metrics, and visualizes trends.

## What it does
- Loads monthly financials from `monthly_financials.csv`
- Cleans/standardizes column names
- Aggregates revenue by month
- Calculates month-over-month (MoM) growth
- Prints a KPI summary to the terminal
- Plots a monthly revenue trend chart

## Tech Stack
- Python 3
- Pandas
- Matplotlib

## Project Structure
code/
├── kpi_dashboard.py
└── monthly_financials.csv

## How to Run
From the `code/` folder:

```bash
cd /Users/jackmaitland/code
python3 -m pip install --user pandas matplotlib
python3 kpi_dashboard.py
