#!/usr/bin/env python3

import telebot, os, types

bot = telebot.TeleBot(os.environ.get('TGBOT_TOKEN'))
bot_commands = types.SimpleNamespace()

bot_commands.ferens = 'ЧО ЭТО?'
bot_commands.degenetard = 'КТО ТАКОЙ degenetard?'
bot_commands.love_mtuci = 'ЛЮБЛЮ МТУСИ КАК degenetard!'
bot_commands.avantgarde = 'ХОЧУ СТАТЬ АДЕПТОМ АВАНГАРДА!'
# bot_commands.songlist = 'ЧТО ЕЩЁ МОЖЕТ ПРЕДОСТАВИТЬ degenetard?'

@bot.message_handler(commands = [ 'start' ])
def start_message(message: telebot.types.Message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row(
        bot_commands.ferens,
        bot_commands.degenetard,
        bot_commands.love_mtuci,
        bot_commands.avantgarde,
        # bot_commands.songlist
    )
    bot.send_message(
        message.chat.id,
        'ПРИВЕТ! ХОЧЕШЬ УЗНАТЬ О ФЕНОМЕНЕ СТУДЕНТА МТУСИ И ПОЗНАКОМИТЬСЯ С ГЕНИЕМ АВАНГАРДА - degenetard?',
        reply_markup = keyboard
    )

@bot.message_handler(commands = [ 'help' ])
def help_message(message: telebot.types.Message):
    bot.send_message(
        message.chat.id,
        'СТУДЕНТ МТУСИ - ЭТО ПОЛОВАЯ ОРИЕНТАЦИЯ, А КОМАНДА /help ДЛЯ СТУДЕНТОВ МЭИ'
    )

@bot.message_handler(content_types = [ 'text' ])
def answer(message: telebot.types.Message):
    match message.text:
        case bot_commands.ferens:
            bot.send_message(
                message.chat.id,
                '"ЧО ЭТО?" - КОМПОЗИЦИЯ ВИА ИМ. ВЛАДИМИРА ФЕРЕНСА: https://youtu.be/JH8-kwRMx-I'
            )
        case bot_commands.degenetard:
            bot.send_message(message.chat.id, 'ГЕНИЙ')
            with open('genius.jpg', 'rb') as genius_file:
                bot.send_photo(message.chat.id, genius_file)
        case bot_commands.love_mtuci:
            bot.send_message(
                message.chat.id,
                'ПРОСЛУШАЙ ГИМН МТУСИ И ПОДДЕРЖИ ГЕНИЯ АВАНГАРДА БИТКОИНАМИ! https://vk.com/wall-183738002_9'
            )
        case bot_commands.avantgarde:
            bot.send_message(
                message.chat.id,
                'ПОДПИШИСЬ: https://vk.com/degenetard'
            )

bot.polling()
