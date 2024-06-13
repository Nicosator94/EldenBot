from utils import *

async def startboss(ctx, boss_name):
	if boss_name is None:
		await ctx.send("This command need a Boss name at parameter !")
		return
	data = get_data()
	author = str(ctx.author)
	if author not in data:
		create_new_player(author, data)
	if boss_name not in data[author]["Boss"]:
		create_boss(boss_name, data[author])
	boss = is_start(author, data)
	if boss is False:
		data[author]["Boss"][boss_name]["Status"] = "Start"
		await ctx.send(f"{boss_name} has been start with {data[author]['Boss'][boss_name]['CountDeath']} !")
	else:
		await ctx.send(f"The \'{boss}\' is already started !")
	push_data(data)