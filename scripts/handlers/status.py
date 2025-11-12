from . import postgres


def show():
    """Показывает статус всех БД"""
    postgres.check_status()
