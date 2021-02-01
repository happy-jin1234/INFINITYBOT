import discord
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
import os
import koreanbots

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command("help")
token = ""
Bot = koreanbots.Client(bot, '')
status = cycle(['.help', f'서버:{len(bot.guilds)}개/유저:{len(bot.users)}명과 함께', '이 메세지를 10초마다 다르게'])

for filename in os.listdir("Cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"Cogs.{filename[:-3]}")
        
@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(status=discord.Status.online,activity=discord.Game(next(status)))

@bot.event
async def on_ready():
    print(f'Main\n{bot.user}')
    change_status.start()

bot.run(token)
