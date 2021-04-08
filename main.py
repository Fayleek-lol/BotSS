import telebot

bot = telebot.TeleBot('1756217731:AAFJZYYU9GrQezzgSrHCHOdZ1hvW0Cg5Zoo')
keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard.row('start')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Привет', 'Пока')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('Планеты', 'Солнечная система', 'Спутники', 'Солнце', 'МКС', 'Пока')
keyboard3 = telebot.types.ReplyKeyboardMarkup(True)
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
                         " Это самый короткий среди всех планет Солнечной системы."
                         "Масса Меркурия составляет - 3,285E23 кг "
                         "Спутники - отсутствуют")
        sti = open('Меркурий.jpg', 'rb')
        bot.send_sticker(message.chat.id, sti)
    elif message.text == "Венера":
        bot.send_message(message.from_user.id,
                         "Венера — вторая по удалённости от Солнца и шестая по размеру планета Солнечной системы,"
                         "наряду с Меркурием, Землёй и Марсом принадлежащая к семейству планет земной группы."
                         "Названа в честь древнеримской богини любви Венеры. "
                         "По ряду характеристик — например, по массе и размерам — Венера считается «сестрой» Земли."
                         "Венерианский год составляет 224,7 земных суток. "
                         "Она имеет самый длинный период вращения вокруг своей оси  среди всех планет Солнечной системы"
                         "И вращается в направлении, противоположном направлению вращения большинства планет."
                         "Масса Венеры составляет - 4,867E24 кг"
                         "Спутники - отсутствуют")
        sti = open('Венера.jpg', 'rb')
        bot.send_sticker(message.chat.id, sti)
    elif message.text == "Земля":
        bot.send_message(message.from_user.id,
                         "Земля — третья по удалённости от Солнца планета Солнечной системы. Самая плотная, "
                         "пятая по диаметру и массе среди всех планет и крупнейшая среди планет земной группы,"
                         " в которую входят также Меркурий, Венера и Марс."
                         " Единственное известное человеку в настоящее время тело Солнечной системы "
                         "в частности и Вселенной вообще, населённое живыми организмами.Планета является домом примерно"
                         "для 8,7 млн видов живых существ, включая человека. "
                         "Территория Земли поделена человечеством на 195 независимых "
                         "государств или 252 страны, взаимодействующих между собой."
                         "Масса - 5,972E24 кг"
                         "Спутники - Луна")
        sti = open('Земля.jpg', 'rb')
        bot.send_sticker(message.chat.id, sti)
    elif message.text == "Марс":
        bot.send_message(message.from_user.id,
                         "Марс — четвёртая по удалённости от Солнца и седьмая по размеру планета Солнечной системы; "
                         "Масса планеты составляет 10,7 % массы Земли."
                         "Названа в честь Марса — древнеримского бога войны, соответствующего древнегреческому Аресу."
                         "Иногда Марс называют красной планетой из-за красноватого оттенка поверхности"
                         "Марс — планета земной группы с разреженной атмосферой,"
                         "Давление на поверхности в 160 раз меньше земного"
                         "Масса Марса составляет - 6,39E23 кг"
                         "Спутники - Деймос, Фобос")
        sti = open('Марс.jpg', 'rb')
        bot.send_sticker(message.chat.id, sti)
    elif message.text == "Юпитер":
        bot.send_message(message.from_user.id,
                         "Юпи́тер — крупнейшая планета Солнечной системы, пятая по удалённости от Солнца. "
                         "Наряду с Сатурном, Ураном и Нептуном, Юпитер классифицируется как газовый гигант."
                         "Планета была известна людям с глубокой древности, что нашло своё отражение в мифологии"
                         "Современное название Юпитера происходит от имени древнеримского верховного бога-громовержца"
                         "Масса Юпитера в 2,47 раза превышает массу всех остальных планет Солнечной системы"
                         "Спутники - Европа, Ио, Ганимед, Каллисто")
        sti = open('Юпитер.jpg', 'rb')
        bot.send_sticker(message.chat.id, sti)
    elif message.text == "Сатурн":
        bot.send_message(message.from_user.id,
                         "Сатурн — шестая планета от Солнца и вторая по размерам планета в Солнечной системе."
                         " Сатурн, а также Юпитер, Уран и Нептун, классифицируются как планеты-гиганты. "
                         "Сатурн назван в честь римского бога земледелия."
                         "В основном Сатурн состоит из водорода, с примесями гелия и следами воды, метана, аммиака."
                         "Внутренняя область представляет собой относительно небольшое ядро из железа, никеля и льда,"
                         "покрытое тонким слоем металлического водорода и газообразным внешним слоем."
                         "Масса Сатурна составляет - 5,683E26 кг "
                         "Спутники -  Мимас, Энцелад, Тефия, Диона, Рея, Титан и Япет")
        sti = open('Сатурн.jpg', 'rb')
        bot.send_sticker(message.chat.id, sti)
    elif message.text == "Уран":
        bot.send_message(message.from_user.id,
                         "Уран — планета Солнечной системы, седьмая по удалённости от Солнца,"
                         "третья по диаметру и четвёртая по массе."
                         "Была открыта в 1781 году английским астрономом Уильямом Гершелем."
                         "Названа в честь греческого бога неба Урана."
                         "Уран стал первой планетой, обнаруженной в Новое время и при помощи телескопа"
                         "Масса Урана составляет - 8,681E25 кг"
                         "Спутники -  Миранда, Ариэль, Умбриэль, Титания и Оберон")
        sti = open('Уран.jpg', 'rb')
        bot.send_sticker(message.chat.id, sti)
    elif message.text == "Нептун":
        bot.send_message(message.from_user.id,
                         "Нептун — восьмая и самая дальняя от Солнца и Земли планета Солнечной системы."
                         "Его масса больше чем у Земли в 17,2 раза и является третьей среди планет Солнечной системы,"
                         "А по экваториальному диаметру Нептун занимает четвёртое место, превосходя Землю в 3,9 раза."
                         "Планета названа в честь римского бога морей."
                         "В атмосфере Нептуна бушуют самые сильные ветры среди планет Солнечной системы. "
                         "По некоторым оценкам, их скорости могут достигать 600 м/с"
                         "Масса Нептуна составляет - 1,024E26 кг"
                         "Спутники - Тритон, Нереида, Протей")
        sti = open('Нептун.jpg', 'rb')
        bot.send_sticker(message.chat.id, sti)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
