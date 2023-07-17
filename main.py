import telebot
import time
from telebot import types

token="Your token"
bot=telebot.TeleBot(token)
triger = 0
i = 1800

@bot.message_handler(commands=['start']) # create command start
def start_message(message): # message for user
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Server is down")
    button2 = types.KeyboardButton("Channel link")
    markup.add(button1, button2)
    bot.reply_to(message, "Hello, " + message.from_user.first_name + ". Answers to questions in the channel", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    global triger
    global i
    if(message.from_user.id == ADMIN_ID):
        bot.send_message(LINK TO THE CHANNEL, message.text)
    if(message.text == "Server is down" and i == 1800):
        bot.send_message(message.chat.id, text="We are working on a problem")
        triger = 1
    elif(message.text == "Channel link"):
        bot.send_message(message.chat.id, text="Link to the channel")
    if triger == 1:
        bot.send_message(ADMIN_ID, "Server is down")
        triger = 0
        for i in range(1800,0,-1):
            time.sleep(1)
            if i == 1800:
                bot.send_message(message.chat.id, "Wait 30 minutes before sending another request")
            if i == 1:
                bot.send_message(message.chat.id, "30 minutes have passed. You can submit the following request.")
        i = 1800

bot.infinity_polling()


