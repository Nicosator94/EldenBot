from utils import *

async def add(ctx):
	data = getData()
	author = str(ctx.author)
	if author not in data:
		CreateNewPlayer(author, data)
	data[author]["CountDeath"] += 1
	boss = isStart(author, data)
	if boss is not False:
		data[author]["Boss"][boss]["CountDeath"] += 1
	pushData(data)