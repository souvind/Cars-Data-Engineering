# Cars Data Engineering Project 🚗

## Overview
Beginner-friendly Data Engineering pipeline:
- Extract car dataset (CSV)
- Transform & clean data using Python
- Load into PostgreSQL
- Optional Power BI dashboard

## Project Structure
```
cars-data-engineering/
├── data/
│   ├── raw/               # Original CSV
│   └── processed/         # Cleaned CSV
├── scripts/               # ETL + SQL scripts
├── dashboard/             # Visualization files
├── README.md
└── requirements.txt
```

## Steps to Run
1. **Clone repo**
```bash
git clone https://github.com/yourusername/cars-data-engineering.git
cd cars-data-engineering
```
2. **Install dependencies**
```bash
pip install -r requirements.txt
```
3. **Create PostgreSQL database**
```sql
CREATE DATABASE carsdb;
\c carsdb
\i scripts/create_tables.sql
```
4. **Run ETL**
```bash
python scripts/etl_cars.py
```
5. **Load to DB**
```bash
python scripts/load_to_db.py
```

## Dataset Source
Sample cars data from Kaggle.
