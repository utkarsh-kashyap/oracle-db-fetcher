import os
from dotenv import load_dotenv
import oracledb

load_dotenv()  # loads .env

class OracleDB:
    """Handles Oracle DB connections using env vars."""

    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT", "1521")
        self.service = os.getenv("DB_SERVICE_NAME")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")

        if not all([self.host, self.port, self.service, self.user, self.password]):
            raise RuntimeError("Missing DB configuration in .env")

        self.dsn = f"{self.host}:{self.port}/{self.service}"

    def fetch_query(self, sql: str, params: dict = None):
        """Run query and return list of dicts."""
        conn = oracledb.connect(user=self.user, password=self.password, dsn=self.dsn)
        cursor = conn.cursor()
        cursor.execute(sql, params or {})
        cols = [col[0] for col in cursor.description] if cursor.description else []
        results = [dict(zip(cols, row)) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return results
