from utils import *

async def add(ctx):
	data = get_data()
	author = str(ctx.author)
	if author not in data:
		await ctx.send("You don't have a profile !")
		return
	data[author]["CountDeath"] += 1
	boss = is_start(author, data)
	if boss is not False:
		data[author]["Boss"][boss]["CountDeath"] += 1
	push_data(data)