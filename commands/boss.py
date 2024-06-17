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
	await ctx.send(f"You have created {name}")

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
	if boss is False or boss == name:
		data[author]["Boss"][name]["Status"] = "Start"
		push_data(data)
		btn = ProgressButton(ctx, author)
		while btn.button_pressed == None:
			message = await ctx.author.send(f"{name} in progress", view=btn)
			btn.message = message
			await btn.wait()
			if btn.button_pressed == "kill":
				data = get_data()
				data[author]["Boss"][name]["Status"] = "Kill"
				push_data(data)
			elif btn.button_pressed == "pause":
				data = get_data()
				data[author]["Boss"][name]["Status"] = "Pause"
				push_data(data)
			else:
				btn = ProgressButton(ctx, author)
	else:
		await ctx.send(f"{boss} is already in progress !")

# ======================================
# Function to delete a boss
# ======================================

async def delete_boss(ctx, name):
	data, author = await validate_boss_and_data(ctx, name, False)
	if data is None:
		return
	btn = ConfirmationButton()
	message = await ctx.author.send(f"Are you sure you want to delete {name} ?", view=btn)
	btn.message = message
	await btn.wait()
	if btn.button_pressed == True:
		author = str(ctx.author)
		del data[author]["Boss"][name]
		await ctx.send(f"{name} has been deleted")
		push_data(data)
	else:
		await ctx.send("You canceled")

# ======================================
# Function to rename a boss
# ======================================

async def rename_boss(ctx, name, new_name):
	if new_name.replace(" ", "").isalpha() is False:
		await ctx.send("The new name can only contain letters and spaces")
		return
	data, author = await validate_boss_and_data(ctx, name, False)
	if data is None:
		return
	for boss in data[author]["Boss"]:
		if boss == new_name:
			await ctx.send(f"{new_name} already exists")
			return
		elif boss == name:
			find = "\"" + name + "\": " + str(data[author]["Boss"][boss]).replace("\'", "\"")
			replace = find.replace("\"" + name + "\": {", "\"" + new_name + "\": {")
	new_data = json.dumps(data)
	new_data = new_data.replace(find, replace)
	data = json.loads(new_data)
	push_data(data)
	await ctx.send(f"You have correctly renamed {name} by {new_name}")