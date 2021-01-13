import discord
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
import asyncio
import os
import koreanbots
import cpuinfo

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command("help")
토큰 = ""
embedcolor = 0xffff33
embederrorcolor = 0xff0000
Bot = koreanbots.Client(bot, '')
cpu = cpuinfo.get_cpu_info()

for filename in os.listdir("Cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"Cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    print(f'Main\n{bot.user.name}')
    Data = await Bot.getBot('765535083124752394')
    status = cycle(['.help', f'서버:{len(bot.guilds)}개/유저:{len(bot.users)}명이랑 함께', '이 메세지를 10초마다 다르게'])
    @tasks.loop(seconds=10)
    async def change_status():
        await bot.change_presence(status=discord.Status.online,activity=discord.Game(next(status)))
    change_status.start()

bot.run(토큰)