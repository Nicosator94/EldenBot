import discord
from discord.ext import commands
import sys
import json
import create
import button
import icons

with open("token.txt","r",encoding="utf-8") as fichier :
	token= fichier.readline()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
	print(f"{bot.user.name} est prêt.")

def isStart(name, data):
	if name in data:
		if "Boss" in data[name]:
			for Boss in data[name]["Boss"]:
				if data[name]["Boss"][Boss]["Status"] == "Start":
					return Boss
	return False

@bot.command(help="Add death")
async def add(ctx):
	with open("count.json", "r") as file:
		data = json.load(file)
	author = str(ctx.author)
	if author not in data:
		create.CreateNewPlayer(author, data)
	data[author]["CountDeath"] += 1
	boss = isStart(author, data)
	if boss is not False:
		data[author]["Boss"][boss]["CountDeath"] += 1
	with open("count.json", "w") as file:
		json.dump(data, file, indent=4)

@bot.command(help="Reset profile")
async def reset(ctx):
	but = button.Button()
	await ctx.message.delete()
	await ctx.send("Are you sure to reset ?", view=but)
	await but.wait()
	if but.button_pressed == True:
		with open("count.json", "r") as file:
			data = json.load(file)
		author = str(ctx.author)
		if author in data:
			del data[author]
		await ctx.send("Your profile has been deleted", delete_after=3)
		with open("count.json", "w") as file:
			json.dump(data, file, indent=4)

@bot.command(help="Add boss")
async def addboss(ctx, boss_name = None):
	if boss_name is None:
		await ctx.send("This command need a Boss name at parameter !")
		return
	with open("count.json", "r") as file:
		data = json.load(file)
	author = str(ctx.author)
	if author not in data:
		create.CreateNewPlayer(author, data)
	if boss_name not in data[author]:
		create.CreateNewBoss(boss_name, data[author])
	else:
		await ctx.send("This boss already exist !")
	with open("count.json", "w") as file:
		json.dump(data, file, indent=4)

@bot.command(help="Start boss")
async def startboss(ctx, boss_name = None):
	if boss_name is None:
		await ctx.send("This boss is not created !")
		return
	with open("count.json", "r") as file:
		data = json.load(file)
	author = str(ctx.author)
	if author not in data:
		create.CreateNewPlayer(author, data)
	if boss_name not in data[author]["Boss"]:
		create.CreateNewBoss(boss_name, data[author])
	boss = isStart(author, data)
	if boss is False:
		data[author]["Boss"][boss_name]["Status"] = "Start"
		await ctx.send(f"{boss_name} has been start with {data[author]['Boss'][boss_name]['CountDeath']} !")
	else:
		await ctx.send(f"The \"{boss}\" is already started !")
	with open("count.json", "w") as file:
		json.dump(data, file, indent=4)

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return

	print(f'{message.author}: {message.content} in {message.channel}')
	await bot.process_commands(message)

bot.run(token)