from utils import *
from disc_utils import *

# ======================================
# Function to create a profile
# ======================================

async def create(ctx):
	data = get_data()
	author = str(ctx.author)
	if author not in data:
		create_new_player(author, data)
		await ctx.send("You have created your profile")
	else:
		await ctx.send("You already have a profile")
	push_data(data)