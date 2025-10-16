from sqlalchemy import create_engine, text
from app.config import settings


class DatabaseManager:
    def __init_(self):
        self.engine = None

    def connect(self):
        try:
            self.engine = create_engine(settings.database_url)
            with self.engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            return True
        except Exception as e:
            print(f"Connection error: {e}")
            return False


db_manager = DatabaseManager()
