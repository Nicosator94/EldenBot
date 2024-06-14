from utils import *
from disc_utils import *

# ======================================
# Function to add a boss
# ======================================

async def add_boss(ctx, name):
	data, author = await validate_boss_and_data(ctx, name, True)
	if data is None:
		return
	create_boss(name, data[author])
	push_data(data)

# ======================================
# Function to start a boss
# ======================================

async def start_boss(ctx, name):
	data, author = await validate_boss_and_data(ctx, name, False)
	if data is None:
		return
	if data[author]["Boss"][name]["Status"] == "Kill":
		await ctx.send(f"{name} is dead !")
		return
	boss = is_start(author, data)
	if boss is False:
		data[author]["Boss"][name]["Status"] = "Start"
		push_data(data)
		but = ProgressButton(ctx, author)
		while but.button_pressed == None:
			message = await ctx.send(f"{name} in progress", view=but)
			but.message = message
			await but.wait()
			if but.button_pressed == "kill":
				data = get_data()
				data[author]["Boss"][name]["Status"] = "Kill"
				push_data(data)
			elif but.button_pressed == "pause":
				data = get_data()
				data[author]["Boss"][name]["Status"] = "Pause"
				push_data(data)
			else:
				but = ProgressButton(ctx, author)
	else:
		await ctx.send(f"{boss} is already in progress !")

# ======================================
# Function to remove a boss
# ======================================

async def remove_boss(ctx, name):
	data, author = await validate_boss_and_data(ctx, name, False)
	if data is None:
		return
	but = ConfirmationButton()
	await ctx.send(f"Are you sure to remove {name} ?", view=but)
	await but.wait()
	if but.button_pressed == True:
		author = str(ctx.author)
		del data[author]["Boss"][name]
		await ctx.send(f"{name} has been remove")
		push_data(data)