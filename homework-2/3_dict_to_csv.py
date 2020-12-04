"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv

users_list = [
    {'name': 'Tatiana Larina', 'age': 17, 'job': 'beautiful woman'}, 
    {'name': 'Evgeniy Onegin', 'age': 28, 'job': 'poet'}, 
    {'name': 'Vladimir Lenski', 'age': 21, 'job': 'student'},
    {'name': 'Olga Larina', 'age': 21, 'job': 'sister'}
]

def main(users_list):
    with open('users_data.csv', 'w', encoding='utf-8', newline='') as my_file:
        fields_names = ['name', 'age', 'job']
        writer = csv.DictWriter(my_file, fields_names, delimiter=';')
        writer.writeheader()
        for user in users_list:
            writer.writerow(user)
    print('Export done!')

if __name__ == "__main__":
    main(users_list)
