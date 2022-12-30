# Бот по загрузки видео с youtube

import os
import re
import datetime

import telebot
from aiogram import *
from config import *
from pytube import YouTube
from pytube import Playlist

bot = telebot.TeleBot(TOKEN)

def writes_logs(_ex):
    with open('logs.log', 'a') as file_log:
        file_log.write('\n' + str(datetime.datetime.now()) + ': ' + str(_ex))

def create_audio(url):
    try:
        yt = YouTube(url).streams.filter(only_audio=True).first()
        path = yt.download("music")
        audio = open(path, 'rb')
        return audio
    except Exception as _ex:
        writes_logs(_ex)

def create_video(url):
    try:
        yt = YouTube(url).streams.filter(progressive=True).first()
        path = yt.download("video")
        video = open(path, 'rb')
        return video
    except Exception as _ex:
        writes_logs(_ex)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! \nКидай ссылку и выберай, что будем скачивать:\n\
1- аудио, 2 - видео. (после цифры через пробел кидай ссылку)")
    
@bot.message_handler(content_types=['text'])
def get_files(message):
    if message.text[:40] == '1 https://www.youtube.com/playlist?list=':
        playlist = Playlist(message.text)
        for url in playlist:
            try:
                audio = create_audio(url)
                bot.send_audio(message.chat.id, audio)
            except Exception as _ex:
                writes_logs(_ex)
    elif message.text[:34] == '1 https://www.youtube.com/watch?v=' or message.text[:19] == '1 https://youtu.be/':
        try:
            url = message.text
            audio = create_audio(url)
            bot.send_audio(message.chat.id, audio)
        except Exception as _ex:
            writes_logs(_ex)
    elif message.text[:34] == '2 https://www.youtube.com/watch?v=' or message.text[:19] == '2 https://youtu.be/':
        try:
            url = message.text
            video = create_video(url)
            bot.send_video(message.chat.id, video)
        except Exception as _ex:
            writes_logs(_ex)

bot.infinity_polling()




