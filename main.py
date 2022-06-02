import telebot
from telebot import types

import ln
import mail
import os
import qrcode

with open("token.dat") as file:
    token = file.read()

bot = telebot.TeleBot(token) # creating a instance

mail_flag = False
chat_id = 0
@bot.message_handler(commands = ['greet','start'])
def greet(message):
    msg = "Steuern sind Raub!"
    bot.reply_to(message, msg)

@bot.message_handler(regexp="get_mail\s\S")
def get_email(message):
    username = message.text.split()[1]
    print(username)
    invoice = ln.get_invoice(2100)
    img = qrcode.make(invoice[0])
    img.save("qr.png")
    photo = open("qr.png", "rb")
    bot.send_message(message.chat.id, invoice[0])
    bot.send_photo(message.chat.id, photo)




bot.polling() # looking for message