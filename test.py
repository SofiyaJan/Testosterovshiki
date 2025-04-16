import psycopg2
conn = psycopg2.connect(
    dbname="testosterovshiki",
    user="postgres",
    password="postgres",
    host="localhost",
    port=5432
)
print("✅ Connected")
