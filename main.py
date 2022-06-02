import telebot
from telebot import types
import db.db
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
    bot.send_message(message.chat.id, "Please wait while your request is processed...")
    invoice = ln.get_invoice(2100)
    img = qrcode.make(invoice[0])
    img.save("qr.png")
    photo = open("qr.png", "rb")
    db.db.save_hash(message.chat.id, invoice[1])
    bot.send_message(message.chat.id, "Please pay this 2100 Sat invoice and send /check when you're done:")
    bot.send_message(message.chat.id, invoice[0])
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=["check"])
def checkPayment(message):
    rhash = db.db.get_hash(message.chat.id)
    status = ln.check_invoice(rhash)
    if status:
        bot.send_message(message.chat.id, "Payment Successful")
    else:
        bot.send_message(message.chat.id, "No payment recieved")



bot.polling() # looking for message