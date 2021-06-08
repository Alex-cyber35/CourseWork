import telebot
import my_parser

TOKEN = '1790327839:AAGNSa5Yi0f3sENq0IhcY5AO0TgFvCyB4_k'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['air_check'])
def get_air_check(message):
    ListOfData = my_parser.func()

    bot.send_message(

        message.chat.id,
        ('Показатель качества воздуха на данный момент:\t ' + str(ListOfData[0]) + '\nВремя последнего обновления: ' + str(ListOfData[1]))
    )


@bot.message_handler(commands=['info'])
def get_air_check(message):

    bot.send_message(

        message.chat.id, "0-50 - ХОРОШО\n" "51-100 - УДОВЛИТВОРИТЕЛЬНОЕ\n" "101-150 - НЕЗДОРОВЫЙ ДЛЯ ЧУВСТВИТЕЛЬНЫХ ГРУПП\n"
                         "151-200 - НЕЗДОРОВЫЙ\n" "201-300 - ОЧЕНЬ НЕЗДОРОВЫЙ\n" "300+ - ОПАСНЫЙ"
    )


@bot.message_handler(content_types=['text'])
def get_text(message):

    bot.send_message(

        message.chat.id,
        'Пожалуйста, отправьте мне команду /air_check чтобы узнать статистику \n'
        'Также вы можете ознакомиться с критерием качества воздуха при помощи команды /info'
    )


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)