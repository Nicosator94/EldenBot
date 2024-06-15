import discord
from discord.ext import commands
from commands.create import *
from commands.add import *
from commands.delete import *
from commands.boss import *
from commands.list import *
from commands.clear import *

def main():

	with open("token.txt", "r", encoding="utf-8") as file :
		token = file.readline()

	intents = discord.Intents.default()
	intents.message_content = True
	bot = commands.Bot(command_prefix='!', intents=intents)

	@bot.event
	async def on_ready():
		print(f"{bot.user.name} est prêt.")

	@bot.command(name="create", help="Create your profile")
	async def create_command(ctx):
		await create(ctx)

	@bot.command(name="add", help="Add death")
	async def add_command(ctx):
		await add(ctx)

	@bot.command(name="delete", help="Delete your profile")
	async def delete_command(ctx):
		await delete(ctx)

	@bot.command(name="boss", help="Boss commands\nUsage: \n"
		"- !boss add [name]: Add a new boss with the given name.\n"
		"- !boss start [name]: Start the boss with the given name.\n"
		"- !boss delete [name]: Delete the boss with the given name.")
	async def boss_command(ctx, param = None, name = None):
		if param is None or name is None:
			await ctx.send("Invalid command !\n"
				"Example of a valid command: !boss [param] [name].")
			return
		if param == "add":
			await add_boss(ctx, name)
		elif param == "start":
			await start_boss(ctx, name)
		elif param == "delete":
			await delete_boss(ctx, name)
		else:
			await ctx.send("Invalid parameter !\nPlease use one of the following: add, start, delete.")
			return

	@bot.command(name="list", help="List of boss, death and status, can take name as parameter")
	async def list_command(ctx, name = None):
		await list(ctx, name)

	@bot.command(name="clear", help="Clear message with number")
	async def clear_command(ctx, amount = None):
		await clear(ctx, amount)

	@bot.event
	async def on_message(message):
		if message.author == bot.user:
			return
		print(f'{message.author}: {message.content} in {message.channel}')
		await bot.process_commands(message)

	bot.run(token)

if __name__ == '__main__':
    main()