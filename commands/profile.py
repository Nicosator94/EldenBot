from utils import *
from disc_utils import *

# ======================================
# Function to create a profile
# ======================================

async def create_profile(ctx, name):
	if name is None:
		await ctx.send("Invalid command !\nExample of a valid command: !create [name]")
		return
	data, user = get_data_user(ctx.author)
	profile = get_profile(name, data[user])
	if profile is not None:
		await ctx.send("The profile already exists")
		return
	data[user]["Profiles"].append({"Name": name, "Deaths": 0, "Current": None, "Bosses": []})
	await ctx.send("You have created your profile")
	if data[user]["Current"] is None:
		data[user]["Current"] = name
		await ctx.send("This profile was chosen by default")
	push_data(data)

# ======================================
# Function to rename a profile
# ======================================

async def rename_profile(ctx, name, new_name):
	if name is None or new_name is None:
		await ctx.send("Invalid command !\nExample of a valid command: !rename [name] [new_name]")
		return
	data, user = get_data_user(ctx.author)
	profile = get_profile(new_name, data[user])
	if profile is not None:
		await ctx.send("A profile already has this name")
		return
	profile = get_profile(name, data[user])
	if profile is None:
		await ctx.send("This profile does not exist")
		return
	if data[user]["Current"] == profile["Name"]:
		data[user]["Current"] = new_name
	profile["Name"] = new_name
	await ctx.send("Your profile has been renamed")
	push_data(data)

# ======================================
# Function to choose a profile
# ======================================

async def choose_profile(ctx, name):
	if name is None:
		await ctx.send("Invalid command !\nExample of a valid command: !choose [name]")
		return
	data, user = get_data_user(ctx.author)
	profile = get_profile(name, data[user])
	if profile is None:
		await ctx.send("This profile does not exist")
		return
	data[user]["Current"] = name
	await ctx.send("You have chosen your profile")
	push_data(data)

# ======================================
# Function to delete a profile
# ======================================

async def delete_profile(ctx, name):
	if name is None:
		await ctx.send("Invalid command !\nExample of a valid command: !delete [name]")
		return
	data, user = get_data_user(ctx.author)
	profile = get_profile(name, data[user])
	if profile is None:
		await ctx.send("This profile does not exist")
		return
	btn = ConfirmationButton()
	message = await ctx.author.send("Are you sure you want to delete your profile ?", view=btn)
	btn.message = message
	await btn.wait()
	if btn.button_pressed == False:
		await ctx.send("You canceled")
		return
	if data[user]["Current"] == profile["Name"]:
		data[user]["Current"] = None
	data[user]["Profiles"].remove(profile)
	await ctx.send("Your profile has been deleted")
	push_data(data)

# ======================================
# Function to show a list of profile
# ======================================

async def list_profile(ctx):
	data, user = get_data_user(ctx.author)
	description = ""
	for profile in data[user]["Profiles"]:
		icons = "🔴 "
		if profile["Name"] == data[user]["Current"]:
			icons = "🟢 "
		description += "᲼᲼- " + icons + profile["Name"] + " : **" + str(profile["Deaths"]) + "** Deaths\n"
	title = "Profiles of " + user.capitalize()
	embed = discord.Embed(title=title, color=0xffff00, description=description)
	await ctx.send(embed=embed)