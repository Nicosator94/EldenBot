from utils import *

# ======================================
# Function to add a death
# ======================================

async def add(ctx):
	data, user = get_data_user(ctx.author)
	profile = get_profile(data[user]["Current"], data[user])
	if profile is None:
		await embed_message(ctx, "Error !", "You do not have a chosen profile")
		return
	await increase_death(ctx, profile, data)

# ======================================
# Function to increase death
# ======================================

async def increase_death(ctx, profile, data):
	from disc_utils import SimpleButton
	profile["Deaths"] += 1
	boss = get_boss(profile["Current"], profile)
	if boss is not None:
		boss["Deaths"] += 1
	push_data(data)
	if profile["Deaths"] % 5 == 0:
		btn = SimpleButton()
		message = await ctx.author.send("10 Squats now !", view=btn)
		btn.message = message
		await btn.wait()
		return True
	return False