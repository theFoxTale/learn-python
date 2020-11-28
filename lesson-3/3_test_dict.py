from collections import Counter
# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
print('')
print('---- 1 ----')
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

def get_names_count(std_list):
    names_list = {}
    for student in std_list:
        name = student['first_name']
        if name not in names_list:
            names_list[name] = 0
        names_list[name] += 1
    return names_list

names_list = get_names_count(students)
for name in names_list:
    print(f'{name}: {names_list[name]}')


# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
print('')
print('---- 2 ----')
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

def get_most_frequently_names(names_list):
    max_count = 0
    result_name = ""
    for name in names_list:
        if names_list[name] > max_count:
            result_name = name
            max_count = names_list[name]
    return result_name

names_list = get_names_count(students)
res_name = get_most_frequently_names(names_list)
print(f"Самое частое имя среди учеников: {res_name}")


# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
print('')
print('---- 3 ----')
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

for idx, students in enumerate(school_students):
    names_list = get_names_count(students)
    res_name = get_most_frequently_names(names_list)
    print(f"Самое частое имя в {idx+1}-ом классе: {res_name}")


# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
print('')
print('---- 4 ----')
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

def get_gender_distribution(one_class):
    males = 0
    females = 0
    for student in one_class['students']:
        if is_male.get(student['first_name']):
            males += 1
        else:
            females += 1
    return {'males': males, 'females': females}

for one_class in school: 
    genders = get_gender_distribution(one_class)
    print(f'В классе {one_class.get("class")}: {genders.get("females")} девочки и {genders.get("males")} мальчика.')

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
print('')
print('---- 5 ----')
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

max_males = 0
max_males_name = ""

max_females = 0
max_females_name = ""
for one_class in school:
    genders = get_gender_distribution(one_class)
    if genders["females"] > max_females:
        max_females = genders["females"]
        max_females_name = one_class["class"]
    if genders["males"] > max_males:
        max_males = genders["males"]
        max_males_name = one_class["class"]

print (f'Больше всего мальчиков в классе: {max_males_name}')
print (f'Больше всего девочек в классе: {max_females_name}')
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a