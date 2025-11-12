from app.core.database import db_manager


def main():
    print("Testing PostgreSQL connection...")
    if db_manager.connect():
        print("✅ Connected to PostgreSQL successfully!")
    else:
        print("❌ Failed to connect to PostgreSQL")


if __name__ == "__main__":
    main()
