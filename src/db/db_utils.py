import psycopg2
import yaml


def get_db_config():
    with open("config/db.yml", "r") as f:
        return yaml.safe_load(f)

def get_conn():
    db = get_db_config()
    return psycopg2.connect(
        host=db["host"],
        port=db["port"],
        dbname=db["database"],
        user=db["user"],
        password=db["password"],
    )

def exec_get_one(sql, params=None):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchone()