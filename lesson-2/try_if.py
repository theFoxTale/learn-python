balance = 300
price = 200
if balance > price:
    print("Спасибо за покупку!")
else:
    print("Для продолжения работы пополните пожалуйста баланс!")


def get_weather(temperature):
    if temperature < 0:
        return('На улице холодно!')
    elif 0 <= temperature <= 14:
        return('На улице прохладно')
    elif 15 <= temperature <= 25:
        return('На улице тепло')
    else:
        return('На улице жарко')

temperature = -6
print(f'Temperature {temperature}: {get_weather(temperature)}')

temperature = 10
print(f'Temperature {temperature}: {get_weather(temperature)}')

temperature = 21
print(f'Temperature {temperature}: {get_weather(temperature)}')