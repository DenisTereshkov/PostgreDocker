from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

import os
from dotenv import load_dotenv

load_dotenv()


def test_postgres_connection():
    try:
        user = os.getenv('POSTGRES_USER')
        password = os.getenv('POSTGRES_PASSWORD')
        db = os.getenv('POSTGRES_DB')
        database_url = f"postgresql://{user}:{password}@localhost:5432/{db}"
        engine = create_engine(
            database_url,
            echo=True
        )
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1")).fetchone()
            print("Test query result:", result)
            if result == (1,):
                print("PostgreSQL connection test passed.")
                return True
            else:
                print("Unexpected result from query.")
                return False
    except SQLAlchemyError as e:
        print("Failed to connect to PostgreSQL:", e)
        return False


if __name__ == "__main__":
    test_postgres_connection()
