"""
Firulais bot.
"""
import telebot
import logging

# CONSTANTS
TOKEN = ""
TROLLED_USER = "Andrea"
FIRULAIS_BARK = "Guaoo "

if __name__ == '__main__':
    logging.basicConfig(filename='firulais.log', filemode='a+', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s: %(message)s',)
    logging.info("Firulais is running...")

    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(func=lambda message: True)
    def barking(message):
        user = message.from_user.first_name
        if user == TROLLED_USER:
            tokens = message.text.split()
            bark = FIRULAIS_BARK*(len(tokens))
            #bot.reply_to(message, bark)
            bot.send_message(message.chat.id, bark)

    bot.polling()

    logging.info("Firulais has finished!")
