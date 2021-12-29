import os
import telebot

TOKEN = '5010988549:AAH_1XMqggEuwsHLA_EBC-cgnGqGhdPojyQ'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.reply_to(message,"Hello World..!")

@bot.message_handler(commands=['help'])
def send_message(message):
  bot.send_message(message,"Sorry, Still learning..")

bot.polling()
