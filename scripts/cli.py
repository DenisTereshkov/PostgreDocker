import argparse

from handlers import postgres, status


def start_database(db_type):
    """Запускает контейнер с базой данных"""
    if db_type == 'postgres':
        postgres.start()
    # Когда будут БД, добавить сюда:
    # elif db_type == 'mysql':
    #     mysql.start()
    else:
        print(f"Неизвестный тип базы данных: {db_type}")


def stop_database(db_type):
    """Останавливает контейнер с базой данных"""
    if db_type == 'postgres':
        postgres.stop()
    else:
        print(f"Неизвестный тип базы данных: {db_type}")


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
        status.show()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
