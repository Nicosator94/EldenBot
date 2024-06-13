import discord

class Button(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=60)
		self.button_pressed = False

	@discord.ui.button(label="Yes", style=discord.ButtonStyle.success)
	async def button_callback_success(self, interaction, button):
		self.button_pressed = True
		self.stop()
		await interaction.message.delete()
	@discord.ui.button(label="Cancel", style=discord.ButtonStyle.danger)
	async def button_callback_danger(self, interaction, button):
		self.stop()
		await interaction.message.delete()