from pathlib import Path
from src.db.db_utils import get_conn

def rebuild_tables():
    sql = Path("src/db/schema.sql").read_text(encoding="utf-8")

    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)

if __name__ == "__main__":
    rebuild_tables()
    print("Tables rebuilt.")