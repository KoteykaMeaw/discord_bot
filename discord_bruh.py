import discord
from bot_logic import gen_pass
from bot_logic import gen_emodji
from bot_logic import flip_coin
from bot_logic import gameee
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
    if message.content.startswith('как дела?'):
        await message.channel.send("норм") 
    if message.content.startswith('тоже'):
        await message.channel.send("ок")
    if message.content.startswith('вав'):
        await message.channel.send("ваув")
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
    elif message.content.startswith('игра'):
        await message.channel.send(gameee())
    elif message.content.startswith('!help'):
        await message.channel.send('на некоторые сообщения этот бот отвечает,а некоторые повторяет. есть пару компнд - смайлик , монетка , игра , пароль и команда !help.')
    else:
        await message.channel.send(message.content)


@client.event
async def on_member_join(self, member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'Welcome {member.mention} to {guild.name}!'
        await guild.system_channel.send(to_send)


client.run(settings["TOKEN"])
