from utils import *

async def addboss(ctx, boss_name):
	if boss_name is None:
		await ctx.send("This command need a Boss name at parameter !")
		return
	data = get_data()
	author = str(ctx.author)
	if author not in data:
		create_new_player(author, data)
	if boss_name not in data[author]["Boss"]:
		create_boss(boss_name, data[author])
	else:
		await ctx.send("This boss already exist !")
	push_data(data)