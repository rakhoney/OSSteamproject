import discord
import asyncio

from discord.ext import commands

bot = commands.Bot(command_prefix='#', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')


@bot.command()
async def hello(message):
    await message.channel.send('Hi!')
@bot.command()
async def 들어와(message):
    channel = message.author.voice.channel
    await channel.connect()
    await message.channel.send("대구대 봇 입장")

@bot.command()
async def 나가(message):
    await bot.voice_clients[0].disconnect()
    await message.channel.send("대구대 봇 퇴장")

bot.run('Token')
