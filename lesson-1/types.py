# task 1
print('Урок "Типы данных", задание №1.')
a = 2
b = 0.5
print(a + b)

# task 2
print("")
print('Урок "Типы данных", задание №2.')
myName = "АНЯ"
myNameUpd = ( myName.lower() ).capitalize()
print(f"Привет, {myNameUpd}!")

# task 3
print("")
print('Урок "Типы данных", задание №3.')
inputData = input('Введите число от 1 до 10: ')
addDecData = int( inputData.strip() ) + 10
print(f"При увеличении на 10 получится: {addDecData}.")

# task 4
print("")
print('Урок "Типы данных", задание №4.')
userName = input('Введите Ваше имя: ')
userNameUp = (userName.strip()).upper()
print(f"Привет, {userNameUp}! Как дела?")

# task 5
print("")
print('Урок "Типы данных", задание №5.')
print(f"float от '1': {float('1')}")
print(f"int от 2.5: {int( float('2.5') )}")
print(f"bool от 1: {bool(1)}")
print(f"bool от '': {bool('')}")
print(f"bool от 0: {bool(0)}")