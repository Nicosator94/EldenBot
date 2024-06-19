from utils import *
from disc_utils import *

# ======================================
# Function to create a profile
# ======================================

async def create_profile(ctx, name):
	if name is None:
		await embed_message(ctx, "Invalid command !", "Example of a valid command: !create [name]")
		return
	data, user = get_data_user(ctx.author)
	profile = get_profile(name, data[user])
	if profile is not None:
		await embed_message(ctx, "Error !", "The profile already exists")
		return
	data[user]["Profiles"].append({"Name": name, "Deaths": 0, "Current": None, "Bosses": []})
	await embed_message(ctx, "", "You have created your profile")
	if data[user]["Current"] is None:
		data[user]["Current"] = name
		await embed_message(ctx, "", "This profile was chosen by default")
	push_data(data)

# ======================================
# Function to rename a profile
# ======================================

async def rename_profile(ctx, name, new_name):
	if name is None or new_name is None:
		await embed_message(ctx, "Invalid command !", "Example of a valid command: !rename [name] [new_name]")
		return
	data, user = get_data_user(ctx.author)
	profile = get_profile(new_name, data[user])
	if profile is not None:
		await embed_message(ctx, "Error !", "A profile already has this name")
		return
	profile = get_profile(name, data[user])
	if profile is None:
		await embed_message(ctx, "Error !", "This profile does not exist")
		return
	if data[user]["Current"] == profile["Name"]:
		data[user]["Current"] = new_name
	profile["Name"] = new_name
	await embed_message(ctx, "", "Your profile has been renamed")
	push_data(data)

# ======================================
# Function to choose a profile
# ======================================

async def choose_profile(ctx, name):
	if name is None:
		await embed_message(ctx, "Invalid command !", "Example of a valid command: !choose [name]")
		return
	data, user = get_data_user(ctx.author)
	profile = get_profile(name, data[user])
	if profile is None:
		await embed_message(ctx, "Error !", "This profile does not exist")
		return
	data[user]["Current"] = name
	await embed_message(ctx, "", "You have chosen your profile")
	push_data(data)

# ======================================
# Function to delete a profile
# ======================================

async def delete_profile(ctx, name):
	if name is None:
		await embed_message(ctx, "Invalid command !", "Example of a valid command: !delete [name]")
		return
	data, user = get_data_user(ctx.author)
	profile = get_profile(name, data[user])
	if profile is None:
		await embed_message(ctx, "Error !", "This profile does not exist")
		return
	btn = ConfirmationButton()
	message = await ctx.author.send("Are you sure you want to delete your profile ?", view=btn)
	btn.message = message
	await btn.wait()
	if btn.button_pressed == False:
		await embed_message(ctx, "", "You canceled")
		return
	if data[user]["Current"] == profile["Name"]:
		data[user]["Current"] = None
	data[user]["Profiles"].remove(profile)
	await embed_message(ctx, "", "Your profile has been deleted")
	push_data(data)

# ======================================
# Function to show a list of profile
# ======================================

async def list_profile(ctx, n_user):
	data, user = get_data_user(ctx.author)
	if n_user is not None:
		user = n_user
	description = ""
	for profile in data[user]["Profiles"]:
		icons = "🔴 "
		if profile["Name"] == data[user]["Current"]:
			icons = "🟢 "
		description += f"᲼᲼- {icons + profile['Name']} : **{str(profile['Deaths'])}** Deaths\n"
	title = f"Profiles of {user.capitalize()}"
	await embed_message(ctx, title, description)