import telebot

bot = telebot.TeleBot ("8625183654:AAHbJFRw58gT9lXVeIXgLs7ryH_H8yDmyBk")


@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id, "Привет, я даун бот")

bot.polling(none_stop=True)    
    
                     
