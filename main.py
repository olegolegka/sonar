import telebot

bot = telebot.TeleBot(token,parse_mode=None)

@bot.message_handler(commands = ["start","help"])
def start_handler(message):
    bot.reply_to(message,"Привет, я твой новый телеграмм бот")
    print(message.text)


bot.infinity_polling()
