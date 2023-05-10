import discord
from bot_logic import gen_pass
from bot_logic import gen_emodji
from bot_logic import flip_coin
from settings import settings
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('привет'):
        await message.channel.send("привет!")
    elif message.content.startswith('пока'):
        await message.channel.send("пока(")
    elif message.content.startswith('го в рб'):
        await message.channel.send("го")
    elif message.content.startswith('пон'):
        await message.channel.send("в жопе лимон")
    elif message.content.startswith('пароль'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('смайлик'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('монетка'):
        await message.channel.send(flip_coin())
    else:
        await message.channel.send(message.content)

client.run(settings["TOKEN"])