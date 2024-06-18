import discord

# ======================================
# Simple Button
# ======================================

class SimpleButton(discord.ui.View):

	def __init__(self):
		super().__init__(timeout=900)

	async def on_timeout(self):
		for item in self.children:
			item.disabled = True
		await self.message.edit(view=self)

	@discord.ui.button(style=discord.ButtonStyle.secondary, emoji="✅")
	async def button_callback_success(self, interaction, button):
		self.message = interaction.message
		for item in self.children:
			item.disabled = True
		await interaction.message.edit(view=self)
		await interaction.response.defer()
		self.stop()

# ======================================
# Confirmation Button
# ======================================

class ConfirmationButton(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=900)
		self.button_pressed = False

	async def on_timeout(self):
		for item in self.children:
			item.disabled = True
		await self.message.edit(view=self)

	@discord.ui.button(label="Yes", style=discord.ButtonStyle.success)
	async def button_callback_success(self, interaction, button):
		self.message = interaction.message
		self.button_pressed = True
		for item in self.children:
			item.disabled = True
		await interaction.message.edit(view=self)
		await interaction.response.defer()
		self.stop()

	@discord.ui.button(label="Cancel", style=discord.ButtonStyle.danger)
	async def button_callback_danger(self, interaction, button):
		self.message = interaction.message
		for item in self.children:
			item.disabled = True
		await interaction.message.edit(view=self)
		await interaction.response.defer()
		self.stop()

# ======================================
# Progress Button
# ======================================

class ProgressButton(discord.ui.View):
	def __init__(self, ctx):
		super().__init__(timeout=900)
		self.button_pressed = None
		self.ctx = ctx

	async def on_timeout(self):
		await self.message.delete()

	@discord.ui.button(label="Pause", style=discord.ButtonStyle.secondary)
	async def button_callback_pause(self, interaction, button):
		self.button_pressed = "pause"
		for item in self.children:
			item.disabled = True
		await self.message.edit(view=self)
		await interaction.response.defer()
		self.stop()

	@discord.ui.button(label="Death", style=discord.ButtonStyle.danger)
	async def button_callback_death(self, interaction, button):
		from utils import get_data_user
		from utils import get_profile
		from commands.add import increase_death
		self.message = interaction.message
		self.button_pressed = "death"
		await interaction.response.defer()
		data, user = get_data_user(self.ctx.author)
		profile = get_profile(data[user]["Current"], data[user])
		is_squats = await increase_death(self.ctx, profile, data)
		if is_squats is True:
			await self.message.delete()
			self.stop()

	@discord.ui.button(label="✅", style=discord.ButtonStyle.success)
	async def button_callback_kill(self, interaction, button):
		self.button_pressed = "kill"
		for item in self.children:
			item.disabled = True
		await self.message.edit(view=self)
		await interaction.response.defer()
		self.stop()