
# ======================================
# Function to clear message
# ======================================

async def clear(ctx, amount):
	if amount is None:
		await ctx.send("!clear [amount]", delete_after=3)
		return
	try:
		amount = int(amount)
	except Exception:
		await ctx.send("Excepted a number", delete_after=3)
		return
	if amount > 20:
		await ctx.send("Limit is 20", delete_after=3)
		return
	await ctx.channel.purge(limit=amount + 1)