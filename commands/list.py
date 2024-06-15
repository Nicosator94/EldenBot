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
	description = ""
	other = 0
	for boss in data[author]["Boss"]:
		description += "᲼᲼- " + icons[data[author]["Boss"][boss].get("Status")] + " " + \
		boss + " : **" + str(data[author]["Boss"][boss].get("CountDeath")) + "** Deaths\n"
		other += data[author]["Boss"][boss].get("CountDeath")
	other = data[author]["CountDeath"] - other
	description += "\n᲼᲼- Other : **" + str(other) + "** Deaths\n"
	title = author.capitalize() + " : " + str(data[author]["CountDeath"]) + " Deaths"
	embed = discord.Embed(title=title, color=0xffff00, description=description)
	await ctx.send(embed=embed)