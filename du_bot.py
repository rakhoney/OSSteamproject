import discord
import asyncio
from datetime import datetime, timezone
import requests, json
from discord.ext import commands

bot = commands.Bot(command_prefix='#', intents=discord.Intents.all())
client = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')

@bot.command()
async def 안녕(message):
    await message.channel.send('안녕하세요!')
@bot.command()
async def 들어와(message):
    channel = message.author.voice.channel
    await channel.connect()
    await message.channel.send("대구대 봇 입장")

@bot.command()
async def 나가(message):
    await bot.voice_clients[0].disconnect()
    await message.channel.send("대구대 봇 퇴장")

def get_weather(city):
    try:
        base_url = "http://api.weatherapi.com/v1/current.json?key=a7d8f6ef58c145ada4860902232805"
        complete_url = base_url + "&q=" + city
        response = requests.get(complete_url)
        result = response.json()

        city = result['location']['name']
        country = result['location']['country']
        time = result['location']['localtime']
        wcond = result['current']['condition']['text']
        celcius = result['current']['temp_c']
        fahrenheit = result['current']['temp_f']
        fclike = result['current']['feelslike_c']
        fflike = result['current']['feelslike_f']

        embed=discord.Embed(title=f"{city}"' Weather', description=f"{country}", color=0x14aaeb)
        embed.add_field(name="Temprature C°", value=f"{celcius}", inline=True)
        embed.add_field(name="Temprature F°", value=f"{fahrenheit}", inline=True)
        embed.add_field(name="Wind Condition", value=f"{wcond}", inline=False)
        embed.add_field(name="Feels Like F°", value=f"{fflike}", inline=True)
        embed.add_field(name="Feels Like C°", value=f"{fclike}", inline=True)
        embed.set_footer(text='Time: 'f"{time}")

        return embed
    except:
        embed=discord.Embed(title="No response", color=0x14aaeb)
        embed.add_field(name="Error", value="Oops!! Please enter a city name", inline=True)
        return embed

@bot.command()
async def weather(message):
        city = message.message.content[9:]
        print(city)

        await message.channel.send(embed=get_weather(city))




bot.run('MTExMTkxNjE5MTM1OTk1OTA3MQ.Gv2I5J.2ICo8oWX78aaJu0VKFeztP55ChskLxr6bvCtH4')
