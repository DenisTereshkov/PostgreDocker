import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Утилита для запуска баз данных в Docker",
        prog="db-util"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        help="Доступные команды"
    )
    start = subparsers.add_parser("start", help="Запустить базу данных")
    start.add_argument(
        "db_type",
        choices=["postgres"],
        help="Тип базы данных"
    )

    stop = subparsers.add_parser('stop', help='Остановить базу данных')
    stop.add_argument(
        'db_type',
        choices=['postgres'],
        help='Тип базы данных'
    )

    subparsers.add_parser('status', help='Показать статус всех баз данных')

    args = parser.parse_args()

    if args.command == 'start':
        print(f"Запускаем {args.db_type}...")
        start_database(args.db_type)
    elif args.command == 'stop':
        print(f"Останавливаем {args.db_type}...")
        stop_database(args.db_type)
    elif args.command == 'status':
        print("Статус баз данных:")
        check_status()
    else:
        parser.print_help()


def start_database(db_type):
    """Запускает контейнер с базой данных"""
    if db_type == 'postgres':
        start_postgres()
    # Когда будут БД, добавить сюда:
    # elif db_type == 'mysql':
    #     start_mysql()
    else:
        print(f"Неизвестный тип базы данных: {db_type}")


def stop_database(db_type):
    """Останавливает контейнер с базой данных"""
    if db_type == 'postgres':
        stop_postgres()
    else:
        print(f"Неизвестный тип базы данных: {db_type}")


def start_postgres():
    """Запускает PostgreSQL контейнер"""
    print("Запускаем PostgreSQL...")
    # TODO: добавить реальный запуск docker-compose
    print("✅ PostgreSQL запущена!")


def stop_postgres():
    """Останавливает PostgreSQL контейнер"""
    print("Останавливаем PostgreSQL...")
    # TODO: добавить реальную остановку
    print("✅ PostgreSQL остановлена!")


def check_status():
    """Показывает статус всех БД"""
    print("PostgreSQL: Не запущена")
    # TODO: добавить реальную проверку статуса


if __name__ == '__main__':
    main()
