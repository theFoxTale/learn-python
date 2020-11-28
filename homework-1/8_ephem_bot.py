"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import settings

from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

def greet_user(update, context):
    print('Вызван /start')
    print(update['message']['text'])
    update.message.reply_text('Здравствуй, пользователь! Ты вызвал команду /start')

def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(f"Ты говоришь Лисичке *{user_text}*.\nИ Лисичка отвечает тебе _{user_text}_!", parse_mode='MARKDOWN')

def print_planet_place(update, context):
    user_text = update.message.text
    text_data = user_text.split()
    if not len(text_data) > 1:
        return update.message.reply_text("Эй, ты забыл дать мне название планеты, так я ничего не найду!")
        
    planet_name = text_data[1].strip()
    if not hasattr(ephem, planet_name):   
        return update.message.reply_text("К сожалению Лисичка не знает такую планету :(")

    #'Mars', 'Earth', 'Mercury', 'Venus', 'Jupiter', 'Neptune', 'Saturn', 'Uranus', 'Pluto'
    planet_data = getattr(ephem, planet_name)
    current_date = date.today()
    planet_data = planet_data(current_date)
    constellation = ephem.constellation( planet_data )
    update.message.reply_text(f'Планета *{planet_name}* сейчас в *{constellation}*.', parse_mode='MARKDOWN')

def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(settings.API_KEY, use_context=True)

    # Обработчики событий
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", print_planet_place))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    # Командуем боту начать ходить в Telegram за сообщениями
    logging.info("Бот стартовал!")
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()


# Исполняется только при прямом вызове файла python bot.py 
# и не вызывается при импорте, например from bot import PROXY
if __name__ == "__main__":
    main()