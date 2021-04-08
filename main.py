import telebot

bot = telebot.TeleBot('1756217731:AAFJZYYU9GrQezzgSrHCHOdZ1hvW0Cg5Zoo')
keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard.row('start')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Привет', 'Пока')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('Планеты', 'Солнечная система', 'Спутники', 'Солнце', 'МКС', 'Пока')
keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row('Меркурий', 'Венера', 'Земля', 'Марс', 'Юпитер', 'Сатурн', ' Уран', 'Нептун', 'Пока')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
                 f'Я бот-гид по Солнечной системе. Приятно познакомиться, {message.from_user.first_name}, и да '
                 f'прибудет с тобой сила!', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id,
                         "Привет! ")
        bot.send_message(message.from_user.id,
                         "О чем ты хочешь узнать?", reply_markup=keyboard2)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    elif message.text == "Пока":
        bot.send_message(message.from_user.id,
                         "Прощай", reply_markup=keyboard)
    elif message.text == "start":
        bot.send_message(message.from_user.id,
                         f'Я бот-гид по Солнечной системе. Приятно познакомиться, {message.from_user.first_name}, и да '
                         f'прибудет с тобой сила!', reply_markup=keyboard1)
    elif message.text == "Планеты":
        bot.send_message(message.from_user.id, "О какой планете ты хочешь узнать?", reply_markup=keyboard3)
    elif message.text == "Меркурий":
        bot.send_message(message.from_user.id,
                         "Меркурий — ближайшая к Солнцу планета Солнечной системы,наименьшая из планет земной группы. "
                         "Названа в честь древнеримского бога торговли — быстрого Меркурия, "
                         "поскольку она движется по небу быстрее других планет."
                         " Её период обращения вокруг Солнца составляет всего 87,97 земных суток"
                         " Это самый короткий среди всех планет Солнечной системы.")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
