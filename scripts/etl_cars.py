import pandas as pd
import os

RAW_PATH = "data/raw/cars.csv"
PROCESSED_PATH = "data/processed/cars_cleaned.csv"

df = pd.read_csv(RAW_PATH)
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

df = df[df['selling_price'] > 1000]
df = df[df['year'] >= 1990]

os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)
df.to_csv(PROCESSED_PATH, index=False)

print(f"Cleaned data saved to {PROCESSED_PATH}")
