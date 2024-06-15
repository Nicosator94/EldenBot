import discord
from utils import *

# ======================================
# Function to show list
# ======================================

async def list(ctx, name):
	author = str(ctx.author)
	if name is not None:
		author = name.lower()
	data = get_data()
	if author not in data:
		await ctx.send(f"{author} doesn't exist")
		return
	description = author.capitalize() + " : **" + str(data[author]["CountDeath"]) + "** Deaths\n"
	for boss in data[author]["Boss"]:
		description += "᲼᲼- " + icons[data[author]["Boss"][boss].get("Status")] + " " + \
		boss + " : **" + str(data[author]["Boss"][boss].get("CountDeath")) + "** Deaths\n"
	embed = discord.Embed(title=author.capitalize() + "\'s list", color=0xffff00, description=description)
	await ctx.send(embed=embed)