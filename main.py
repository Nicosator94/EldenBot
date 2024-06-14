import discord
from discord.ext import commands
from commands.create import *
from commands.add import *
from commands.remove import *
from commands.boss import *
from commands.list import *

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

	@bot.command(name="remove", help="Remove your profile")
	async def remove_command(ctx):
		await remove(ctx)

	@bot.command(name="boss", help="Boss commands\nUsage: \n"
		"- !boss add [name]: Add a new boss with the given name.\n"
		"- !boss start [name]: Start the boss with the given name.\n"
		"- !boss remove [name]: Remove the boss with the given name.")
	async def boss_command(ctx, param = None, name = None):
		if param is None or name is None:
			await ctx.send("Invalid command !\n"
				"Example of a valid command: !boss [param] [name].")
			return
		if param == "add":
			await add_boss(ctx, name)
		elif param == "start":
			await start_boss(ctx, name)
		elif param == "remove":
			await remove_boss(ctx, name)
		else:
			await ctx.send("Invalid parameter !\nPlease use one of the following: add, start, remove.")
			return

	@bot.command(name="list", help="List of boss, death and status")
	async def list_command(ctx):
		await list(ctx)

	@bot.event
	async def on_message(message):
		if message.author == bot.user:
			return

		print(f'{message.author}: {message.content} in {message.channel}')
		await bot.process_commands(message)

	bot.run(token)

if __name__ == '__main__':
    main()