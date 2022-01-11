import telebot
from telebot import types
import random
token = "2122754288:AAGnp3X99n5g_fKA75GBZH5CxM9vvkZoXQI"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я нахожусь на стадии разработки. И вот что я пока что могу: \n'
                                      'Разговорные фразы: '
                                      'Привет, Как дела, Кто твой создатель, Пока \n'
                                      'Команды: '
                                      '/start - Вернуться в начало, \n'
                                      '/help - Список всех команд, \n'
                                      '/money - Курс валют, \n'
                                      '/tickets - Поиск дешевых авиабилетов, \n'
                                      '/games - Не знаете во что поиграть? Я подскажу ')

@bot.message_handler(commands=['money'])
def start_message(message):
    bot.send_message(message.chat.id, "Курсы основных валют: \n"
                                      "1 Доллар США - 74,68 рублей, \n"
                                      "1 Евро - 83,71 рублей, \n"
                                      "1 Фунт стерлингов - 99,54 рублей, \n"
                                      "1 Швейцарский франк - 79,94 рублей, \n"
                                      "1 Шведская крона - 8,2 рублей. ")

@bot.message_handler(commands=['tickets'])
def start_message(message):
    bot.send_message(message.chat.id, "Поезды слишком медленные? Самые дешевые авиабилеты вы можете найти тут - https://www.aviasales.ru/?marker=15468.ydof213322172821&yclid=7021809146448629960")

@bot.message_handler(commands=['games'])
def start_message(message):
    bot.send_message(message.chat.id, "Нравятся шутеры? Тогда попробуйте: PUBG, Call of Duty, Overwatch, CS:GO, Apex .\n"
                                      "По душе стратегии? Выбирайте: FoE, Stellaris, Civilization, Cities: Skylines, .\n"
                                      "Любите рпг? Вот лучшие: Skyrim, Diablo 2, Mass Effect 2, Dragon Age: Origins .\n"
                                      "Надеюсь чем-то вам помог ")
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Информация о МТУСИ", "Другой вопрос", "/help", "Скок см?")
    bot.send_message(message.chat.id, 'Здравствуйте! Чем вам помочь?', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "информация о мтуси":
        bot.send_message(message.chat.id, 'Тогда вам сюда – https://mtuci.ru/')
    elif message.text.lower() == "другой вопрос":
        bot.send_message(message.chat.id, 'Тогда чем я могу вам помочь?')
    elif message.text.lower() == 'скок см?':
        a=random.randint(2, 25)
        if a>18:
            bot.send_message(message.chat.id, "У вас огромный пенис, целых " + str(a) + " см")
        else:
            bot.send_message(message.chat.id, "У вас всего лишь " + str(a) + " см")
    elif message.text == "Привет":
        bot.send_message(message.from_user.id, "Здравствуйте, чем я могу быть вам полезен?")
    elif message.text == "Как дела?" or message.text == "Как дела":
        bot.send_message(message.from_user.id, "Как и всегда, нормально, я же обычный бот, а вы как поживаете?")
    elif message.text == "Кто твой создатель?" or message.text == "Кто твой создатель":
        bot.send_message(message.from_user.id, "Вы можете найти его вот тут - https://vk.com/gh_ds")
    elif message.text == "Пока":
        bot.send_message(message.from_user.id, "До новых встреч, пишите еще!")
    elif message.text == "Саша":
        bot.send_message(message.from_user.id, "Хороший волейболист")
    elif message.text == "Артур":
        bot.send_message(message.from_user.id, "Артур - безмамный казел")
    else:
        bot.send_message(message.from_user.id, "Я вас плохо понял. Введите команду /help.")


bot.polling(none_stop=True, interval=0)