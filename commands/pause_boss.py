from utils import *
from disc_utils import *

async def pauseboss(ctx, boss_name):
	if boss_name is None:
		await ctx.send("This command need a Boss name at parameter !")
		return
	data = get_data()
	author = str(ctx.author)
	if author not in data:
		create_new_player(author, data)
	if boss_name not in data[author]["Boss"]:
		create_boss(boss_name, data[author])
	if "Status" in data[author]["Boss"][boss_name] and data[author]["Boss"][boss_name]["Status"] == "Start":
		data[author]["Boss"][boss_name]["Status"] = "Pause"
	else:
		boss = is_start(author, data)
		if boss is not False:
			but = Button()
			await ctx.send(f"\'{boss}\' is currently in progress !\nDo you want to pause him ?", view=but)
			await but.wait()
			if but.button_pressed == True:
				data[author]["Boss"][boss]["Status"] = "Pause"
		else:
			await ctx.send("No bosses are currently in progress !")
	push_data(data)