import discord
import asyncio
import datetime
import requests, json
from discord.ext import commands
import time
from deep_translator import GoogleTranslator

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
async def 날씨(message):
        city = message.message.content[4:]
        to_translate = city
        translated = GoogleTranslator(source='auto', target='english').translate(to_translate)
        print(city)
        print(translated)
        await message.channel.send(embed=get_weather(translated))
@bot.command()
async def 몇시야(message):
        time = "현재 시간: " + datetime.datetime.now().strftime("%H"+"시"+"%M"+"분")
        await message.channel.send(time)
@bot.command()
async def 무슨요일이야(message):
        to_translate = datetime.date.today().strftime("%A")
        translated = "오늘의 요일: " + GoogleTranslator(source='auto', target='korean').translate(to_translate)
        await message.channel.send(translated)
@bot.command()
async def 날짜(message):
        date = "금일 : " + datetime.datetime.now().strftime("%Y"+"년"+"%m"+"월"+"%d"+"일")
        await message.channel.send(date)
bot.run('token')
