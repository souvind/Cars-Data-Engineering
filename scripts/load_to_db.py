import pandas as pd
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="carsdb",
    user="postgres",
    password="yourpassword",
    port="5432"
)
cur = conn.cursor()

df = pd.read_csv("data/processed/cars_cleaned.csv")

for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO cars (name, year, selling_price, km_driven, fuel, seller_type, transmission, owner)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """, tuple(row))

conn.commit()
cur.close()
conn.close()

print("Data loaded into database successfully!")
