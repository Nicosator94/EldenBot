from utils import *
from disc_utils import *

# ======================================
# Function to remove a profile
# ======================================

async def remove(ctx):
	data = get_data()
	author = str(ctx.author)
	if author not in data:
		await ctx.send("You don't have a profile !")
		return
	but = ConfirmationButton()
	await ctx.send("Are you sure to remove your profile ?", view=but)
	await but.wait()
	if but.button_pressed == True:
		author = str(ctx.author)
		if author in data:
			del data[author]
		await ctx.send("Your profile has been remove")
		push_data(data)