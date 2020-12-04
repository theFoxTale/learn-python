"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime, timedelta
import locale

def print_days():
    locale.setlocale(locale.LC_ALL, "russian")

    dt_now = datetime.now()
    dt_now_printable = dt_now.strftime('%d %B %Y, %A')
    print(f'Сегодняшний день: {dt_now_printable}')

    dt_yesterday = dt_now - timedelta(days=1)
    dt_yesterday_printable = dt_yesterday.strftime('%d %B %Y, %A')
    print(f'Вчерашний день: {dt_yesterday_printable}')

    dt_data = dt_now - timedelta(days=30)
    dt_data_printable = dt_data.strftime('%d %B %Y, %A')
    print(f'День 30 дней назад: {dt_data_printable}')


def str_2_datetime(date_string):
    print('')
    print(f'Строка с числом: {date_string}')

    date_data = datetime.strptime(date_string, '%y/%m/%d %H:%M:%S.%f')
    print(f'Преобразованное число: {date_data}')

    date_data_printable = date_data.strftime("%d.%m.%Y %H:%M:%S")
    print(f'Преобразованное число, другой формат: {date_data_printable}')

if __name__ == "__main__":
    print_days()
    str_2_datetime("01/01/20 12:10:03.234567")
