from utils import *
from disc_utils import *

async def remove(ctx):
	but = Button()
	await ctx.message.delete()
	await ctx.send("Are you sure to remove ?", view=but)
	await but.wait()
	if but.button_pressed == True:
		data = get_data()
		author = str(ctx.author)
		if author in data:
			del data[author]
		await ctx.send("Your profile has been remove", delete_after=3)
		push_data(data)