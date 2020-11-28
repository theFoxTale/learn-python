userName = input('Введите Ваше имя: ')
print( f'Привет, {userName}' )

userAge = input('Сколько Вам сейчас лет: ')
print(f'Тип введённых данных: {type(userAge)};')
yearBorn = 2020 - int(userAge)
print(f'Вы родитись в {yearBorn} году, мои поздравления!')