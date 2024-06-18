from utils import *
from disc_utils import *

# ======================================
# Function to create a boss
# ======================================

async def create_boss(ctx, name):
	if name is None:
		await ctx.send("Invalid command !\nExample of a valid command: !boss create [name]")
		return
	data, user = get_data_user(ctx.author)
	profile = get_profile(data[user]["Current"], data[user])
	if profile is None:
		await ctx.send("You do not have a chosen profile")
		return
	boss = get_boss(name, profile)
	if boss is not None:
		await ctx.send("The boss already exists")
		return
	profile["Bosses"].append({"Name": name, "Deaths": 0, "Status": "Paused"})
	await ctx.send(f"You have created {name}")
	push_data(data)

# ======================================
# Function to rename a boss
# ======================================

async def rename_boss(ctx, name, new_name):
	if name is None or new_name is None:
		await ctx.send("Invalid command !\nExample of a valid command: !boss rename [name] [new_name]")
		return
	data, user = get_data_user(ctx.author)
	profile = get_profile(data[user]["Current"], data[user])
	if profile is None:
		await ctx.send("You do not have a chosen profile")
		return
	boss = get_boss(new_name, profile)
	if boss is not None:
		await ctx.send("A boss already has this name")
		return
	boss = get_boss(name, profile)
	if boss is None:
		await ctx.send("The boss does not exist")
		return
	if profile["Current"] == boss["Name"]:
		profile["Current"] = new_name
	boss["Name"] = new_name
	await ctx.send(f"You have correctly renamed {name} by {new_name}")
	push_data(data)

# ======================================
# Function to start a boss
# ======================================

async def start_boss(ctx, name):
	if name is None:
		await ctx.send("Invalid command !\nExample of a valid command: !boss start [name]")
		return
	data, user = get_data_user(ctx.author)
	profile = get_profile(data[user]["Current"], data[user])
	if profile is None:
		await ctx.send("You do not have a chosen profile")
		return
	boss = get_boss(name, profile)
	if boss is None:
		await ctx.send("The boss does not exist")
		return
	if profile["Current"] != None and profile["Current"] != name:
		await ctx.send("A boss has already started")
		return
	if boss["Status"] == "Killed":
		await ctx.send("The boss is already dead")
		return
	boss["Status"] = "Started"
	profile["Current"] = name
	push_data(data)
	btn = ProgressButton(ctx)
	while btn.button_pressed == None:
		message = await ctx.author.send(f"{name} in progress", view=btn)
		btn.message = message
		await btn.wait()
		if btn.button_pressed == "kill":
			data, user = get_data_user(ctx.author)
			profile = get_profile(data[user]["Current"], data[user])
			boss = get_boss(name, profile)
			boss["Status"] = "Killed"
			profile["Current"] = None
			push_data(data)
		elif btn.button_pressed == "pause":
			data, user = get_data_user(ctx.author)
			profile = get_profile(data[user]["Current"], data[user])
			boss = get_boss(name, profile)
			boss["Status"] = "Paused"
			profile["Current"] = None
			push_data(data)
		else:
			btn = ProgressButton(ctx)

# ======================================
# Function to delete a boss
# ======================================

async def delete_boss(ctx, name):
	if name is None:
		await ctx.send("Invalid command !\nExample of a valid command: !boss delete [name]")
		return
	data, user = get_data_user(ctx.author)
	profile = get_profile(data[user]["Current"], data[user])
	if profile is None:
		await ctx.send("You do not have a chosen profile")
		return
	boss = get_boss(name, profile)
	if boss is None:
		await ctx.send("The boss does not exist")
		return
	btn = ConfirmationButton()
	message = await ctx.author.send(f"Are you sure you want to delete {name} ?", view=btn)
	btn.message = message
	await btn.wait()
	if btn.button_pressed == False:
		await ctx.send("You canceled")
		return
	if profile["Current"] == boss["Name"]:
		profile["Current"] = None
	profile["Bosses"].remove(boss)
	await ctx.send(f"{name} has been deleted")
	push_data(data)

# ======================================
# Function to show a list of boss
# ======================================

async def list_boss(ctx):
	data, user = get_data_user(ctx.author)
	profile = get_profile(data[user]["Current"], data[user])
	if profile is None:
		await ctx.send("You do not have a chosen profile")
		return
	description = ""
	other = 0
	for boss in profile["Bosses"]:
		description += "᲼᲼- " + icons[boss["Status"]] + " " + \
		boss["Name"] + " : **" + str(boss["Deaths"]) + "** Deaths\n"
		other += boss["Deaths"]
	other = profile["Deaths"] - other
	description += "\n᲼᲼- Other : **" + str(other) + "** Deaths\n"
	title = user.capitalize() + " :\n" + profile["Name"] + " : " + str(profile["Deaths"]) + " Deaths"
	embed = discord.Embed(title=title, color=0xffff00, description=description)
	await ctx.send(embed=embed)