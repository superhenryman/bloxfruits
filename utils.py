import psycopg2
import time
import os
import json
from argon2 import PasswordHasher
def hash(string):
    ph = PasswordHasher()
    return ph.hash(string)
def verify(string, hash):
    ph = PasswordHasher()
    return ph.verify(hash, string)
def get_conn():
    database_url = os.getenv("DATABASE_URL")
    retry_count = 5
    for attempt in range(retry_count):
        try:
            conn = psycopg2.connect(database_url)
            print("Connection Established.")
            return conn
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(2 ** attempt)
    raise Exception("Failed to connect to the database after multiple attempts.")

def init_db():
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders(
            id SERIAL PRIMARY KEY,
            order JSONB NOT NULL  
        )""")
        conn.commit()

def insert_order(order):
    order_json = json.dumps(order)
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO orders (order) VALUES (%s)", (order_json,))
        conn.commit()

