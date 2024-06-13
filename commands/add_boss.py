from utils import *

async def addboss(ctx, boss_name):
	if boss_name is None:
		await ctx.send("This command need a Boss name at parameter !")
		return
	data = getData()
	author = str(ctx.author)
	if author not in data:
		CreateNewPlayer(author, data)
	if boss_name not in data[author]:
		CreateNewBoss(boss_name, data[author])
	else:
		await ctx.send("This boss already exist !")
	pushData(data)