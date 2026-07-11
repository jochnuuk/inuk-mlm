from pathlib import Path
import os

from dotenv import load_dotenv
import ibis

load_dotenv()

DB_URL = os.getenv("DB_URL", "duckdb:///data/inukmlm.duckdb")


def ensure_dirs() -> None:
    Path("data").mkdir(exist_ok=True)


def connect_ibis():
    if DB_URL.startswith("duckdb:///"):
        db_path = DB_URL.replace("duckdb:///", "")
        return ibis.duckdb.connect(db_path)
    if DB_URL.startswith("postgresql://"):
        return ibis.postgres.connect(DB_URL)
    raise ValueError(f"Unsupported DB_URL: {DB_URL}")


if __name__ == "__main__":
    ensure_dirs()
    con = connect_ibis()
    print("Connected to:", DB_URL)
    print("Tables:", con.list_tables())
