import discord
from utils import *
from commands.profile import list_profile
from commands.boss import list_boss

# ======================================
# Function to check if user exists
# ======================================

def is_user(user, data):
	for usr in data:
		if user == usr:
			return True
	return False

# ======================================
# Function to display a list of user profiles
# ======================================

async def list(ctx, user, profile):
	data = get_data()
	if user is None:
		description = ""
		for usr in data:
			description += f"᲼᲼- {usr}\n"
		await embed_message(ctx, "Users list :", description)
		return
	if is_user(user, data) is False:
			await embed_message(ctx, "Error !", "The user does not exist")
			return
	if profile is None:
		await list_profile(ctx, user)
		return
	profile = get_profile(profile, data[user])
	if profile is None:
		await embed_message(ctx, "Error !", "This profile does not exist")
		return
	await list_boss(ctx, profile)