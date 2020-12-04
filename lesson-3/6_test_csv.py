import csv

users_list = [
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]

with open('users_data.csv', 'w', encoding='utf-8', newline='') as my_file:
    fields_names = ['name', 'age', 'job']
    writer = csv.DictWriter(my_file, fields_names, delimiter=';')
    writer.writeheader()
    for user in users_list:
        writer.writerow(user)