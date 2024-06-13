import discord
from discord.ext import commands
from commands.add import *
from commands.add_boss import *
from commands.reset import *
from commands.start_boss import *

def main():

	with open("token.txt", "r", encoding="utf-8") as file :
		token = file.readline()

	intents = discord.Intents.default()
	intents.message_content = True
	bot = commands.Bot(command_prefix='!', intents=intents)

	@bot.event
	async def on_ready():
		print(f"{bot.user.name} est prêt.")

	@bot.command(name="add", help="Add death")
	async def add_command(ctx):
		await add(ctx)

	@bot.command(name="reset", help="Reset profile")
	async def reset_command(ctx):
		await reset(ctx)

	@bot.command(name="addboss",help="Add boss")
	async def addboss_command(ctx, boss_name = None):
		await addboss(ctx, boss_name)

	@bot.command(name="startboss", help="Start boss")
	async def startboss_command(ctx, boss_name = None):
		await startboss(ctx, boss_name)

	# @bot.command(help="Pause boss")
	# async def pauseboss(ctx, boss_name = None):
	# 	if boss_name is None:
	# 		await ctx.send("This command need name of the boss !")
	# 		return

	@bot.event
	async def on_message(message):
		if message.author == bot.user:
			return

		print(f'{message.author}: {message.content} in {message.channel}')
		await bot.process_commands(message)

	bot.run(token)

if __name__ == '__main__':
    main()