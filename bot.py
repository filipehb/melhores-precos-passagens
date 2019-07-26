#!/usr/bin/python3
# -*- coding: utf-8 -*-
from telegram.ext import Updater
from telegram.ext import CommandHandler
import os, time, logging
import telegram

my_token = 'TOKEN DO BOT'
logging.basicConfig(filename='bot.log', level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")

#Envio direto a um usuário por seu chat id
def send_direct(msg):
    bot = telegram.Bot(token=my_token)
    bot.send_message(chat_id=0000, text=msg) #Id do seu chat
    logging.info("Sucesso ao enviar msg pelo bot!")

if __name__ == '__main__':
    send_direct('teste')