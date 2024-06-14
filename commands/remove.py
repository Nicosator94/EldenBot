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
	btn = ConfirmationButton()
	message = await ctx.send("Are you sure to remove your profile ?", view=btn)
	btn.message = message
	await btn.wait()
	if btn.button_pressed == True:
		author = str(ctx.author)
		if author in data:
			del data[author]
		await ctx.send("Your profile has been remove")
		push_data(data)
	else:
		await ctx.send("You cancel")