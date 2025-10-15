import os
import time
import psycopg2

db_host = os.environ.get('POSTGRES_HOST', 'db')
db_port = int(os.environ.get('POSTGRES_PORT', 5432))

while True:
    try:
        conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            user=os.environ.get('POSTGRES_USER'),
            password=os.environ.get('POSTGRES_PASSWORD'),
            dbname=os.environ.get('POSTGRES_DB')
        )
        conn.close()
        break
    except psycopg2.OperationalError:
        print("Waiting for PostgreSQL...")
        time.sleep(1)

print("PostgreSQL started")
