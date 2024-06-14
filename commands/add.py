from utils import *

# ======================================
# Function to add a death
# ======================================

async def add(ctx):
	data = get_data()
	author = str(ctx.author)
	if author not in data:
		await ctx.send("You don't have a profile !")
		return
	await increase_death(ctx, data, author)
	push_data(data)

# ======================================
# Function to increase death
# ======================================

async def increase_death(ctx, data, author):
	from disc_utils import SimpleButton
	data[author]["CountDeath"] += 1
	boss = is_start(author, data)
	if boss is not False:
		data[author]["Boss"][boss]["CountDeath"] += 1
	push_data(data)
	if data[author]["CountDeath"] % 5 == 0:
		but=SimpleButton()
		await ctx.send("10 Squats now !", view=but)
		await but.wait()
		await ctx.send("Well done !")