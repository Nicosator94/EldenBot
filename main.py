import discord
from discord.ext import commands
from commands.profile import *
from commands.add import *
from commands.boss import *
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

	@bot.command(name="profile", help="Profile commands\nUsage: \n"
		"- !profile create [name]: Create a new profile with the given name\n"
		"- !profile rename [name] [new_name]: Rename the profile with the given name with the given new name\n"
		"- !profile choose [name]: Choose the profile with the given name\n"
		"- !profile delete [name]: Delete the profile with the given name\n"
		"- !profile list: Shows a list including all profiles")
	async def profile_command(ctx, param = None, name = None, new_name = None):
		match param:
			case "create":
				await create_profile(ctx, name)
			case "rename":
				await rename_profile(ctx, name, new_name)
			case "choose":
				await choose_profile(ctx, name)
			case "delete":
				await delete_profile(ctx, name)
			case "list":
				await list_profile(ctx)
			case _:
				await ctx.send("Invalid command !\nTake a look at !help profile")

	@bot.command(name="add", help="Add death")
	async def add_command(ctx):
		await add(ctx)

	@bot.command(name="boss", help="Boss commands\nUsage: \n"
		"- !boss create [name]: Create a new boss with the given name\n"
		"- !boss rename [name] [new_name]: Rename the boss with the given name with the given new name\n"
		"- !boss start [name]: Start the boss with the given name\n"
		"- !boss delete [name]: Delete the boss with the given name\n"
		"- !boss list: Shows a list including all bosses")
	async def boss_command(ctx, param = None, name = None, new_name = None):
		match param:
			case "create":
				await create_boss(ctx, name)
			case "rename":
				await rename_boss(ctx, name, new_name)
			case "start":
				await start_boss(ctx, name)
			case "delete":
				await delete_boss(ctx, name)
			case "list":
				await list_boss(ctx)
			case _:
				await ctx.send("Invalid command !\nTake a look at !help boss")

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