from utils import *

async def startboss(ctx, boss_name):
	if boss_name is None:
		await ctx.send("This command need name of the boss !")
		return
	data = getData()
	author = str(ctx.author)
	if author not in data:
		CreateNewPlayer(author, data)
	if boss_name not in data[author]["Boss"]:
		CreateNewBoss(boss_name, data[author])
	boss = isStart(author, data)
	if boss is False:
		data[author]["Boss"][boss_name]["Status"] = "Start"
		await ctx.send(f"{boss_name} has been start with {data[author]['Boss'][boss_name]['CountDeath']} !")
	else:
		await ctx.send(f"The \'{boss}\' is already started !")
	pushData(data)