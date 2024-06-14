import discord

class SimpleButton(discord.ui.View):

	@discord.ui.button(style=discord.ButtonStyle.secondary, emoji="✅")
	async def button_callback_success(self, interaction, button):
		await interaction.message.delete()
		self.stop()

class ConfirmationButton(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=60)
		self.button_pressed = False

	@discord.ui.button(label="Yes", style=discord.ButtonStyle.success)
	async def button_callback_success(self, interaction, button):
		self.button_pressed = True
		await interaction.message.delete()
		self.stop()

	@discord.ui.button(label="Cancel", style=discord.ButtonStyle.danger)
	async def button_callback_danger(self, interaction, button):
		await interaction.message.delete()
		self.stop()

class ProgressButton(discord.ui.View):
	def __init__(self, ctx, author):
		super().__init__(timeout=900)
		self.button_pressed = None
		self.ctx = ctx
		self.author = author

	async def on_timeout(self):
		await self.message.delete()

	@discord.ui.button(label="⏸️", style=discord.ButtonStyle.secondary)
	async def button_callback_pause(self, interaction, button):
		self.button_pressed = "pause"
		await interaction.message.delete()
		self.stop()

	@discord.ui.button(label="Death", style=discord.ButtonStyle.danger)
	async def button_callback_death(self, interaction, button):
		from utils import get_data
		from utils import push_data
		from commands.add import increase_death
		self.message = interaction.message
		self.button_pressed = "death"
		await interaction.response.defer()
		data = get_data()
		await increase_death(self.ctx, data, self.author)
		push_data(data)

	@discord.ui.button(label="✅", style=discord.ButtonStyle.success)
	async def button_callback_kill(self, interaction, button):
		self.button_pressed = "kill"
		await interaction.message.delete()
		self.stop()