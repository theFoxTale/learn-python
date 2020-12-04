from datetime import datetime, timedelta
import locale

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


print('')
date_text = "01/01/25 12:10:03.234567"
print(f'Строка с числом: {date_text}')

date_data = datetime.strptime(date_text, '%y/%m/%d %H:%M:%S.%f')
print(f'Преобразованное число: {date_data}')

date_data_printable = date_data.strftime("%d.%m.%Y %H:%M:%S")
print(f'Преобразованное число, другой формат: {date_data_printable}')