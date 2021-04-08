import telebot

bot = telebot.TeleBot('1756217731:AAFJZYYU9GrQezzgSrHCHOdZ1hvW0Cg5Zoo')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Привет', 'Пока')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
                 f'Я бот-гид по Солнечной системе. Приятно познакомиться, {message.from_user.first_name}, и да '
                 f'прибудет с тобой сила!', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id,
                         "Привет!")
        bot.send_message(message.from_user.id,
                         "Вот что я могу:")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    elif message.text == "Пока":
        bot.send_message(message.from_user.id, "Прощай")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)

