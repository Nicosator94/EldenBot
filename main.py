import discord
from discord.ext import commands
import sys
import json

with open("token.txt","r",encoding="utf-8") as fichier :
	token= fichier.readline()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
	print(f"{bot.user.name} est prêt.")

@bot.command()
async def add(ctx):
	with open("count.json", "r") as file:
		data = json.load(file)
	author = str(ctx.author)
	if author not in data:
		data[author] = {"death": 0}
	data[author]["death"] += 1
	await ctx.send(data[author]["death"])
	with open("count.json", "w") as file:
		json.dump(data, file, indent=4)

@bot.command()
async def reset(ctx):
	with open("count.json", "r") as file:
		data = json.load(file)
	author = str(ctx.author)
	if author not in data:
		data[author] = {"death": 0}
	else:
		data[author]["death"] = 0
	await ctx.send(data[author]["death"])
	with open("count.json", "w") as file:
		json.dump(data, file, indent=4)

@bot.command(help='<> - Répond pong')
async def ping(ctx):
	await ctx.send('Pong')

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return

	print(f'{message.author}: {message.content} in {message.channel}')
	await bot.process_commands(message)

bot.run(token)