from utils import *
from disc_utils import *

async def reset(ctx):
	but = Button()
	await ctx.message.delete()
	await ctx.send("Are you sure to reset ?", view=but)
	await but.wait()
	if but.button_pressed == True:
		data = getData()
		author = str(ctx.author)
		if author in data:
			del data[author]
		await ctx.send("Your profile has been deleted", delete_after=3)
		pushData(data)