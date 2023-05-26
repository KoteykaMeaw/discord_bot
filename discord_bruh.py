import discord
from bot_logic import gen_pass
from bot_logic import gen_emodji
from bot_logic import flip_coin
from bot_logic import gameee

from discord.ext import commands

intents=discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_member_join(member):
    print(f'{member} зашёл на сервер.')
    await member.send(f"Привет {member}!")

bot.run('token here')

