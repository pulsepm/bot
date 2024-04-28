import os
import requests

import discord
from discord.ext import commands
from discord import app_commands
from typing import Optional
import asyncio

from bot_github import (
    wiki_article,
    wiki_embed
)

intents = discord.Intents.all()

TOKEN = 'your'

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
	print(f'{bot.user} has connected to Discord!')
	await main()

@bot.tree.command()
@app_commands.describe(
    term='The term you are searching for',
)
async def wiki(interaction: discord.Interaction, term: str):
    """Seeks for a specified term."""
    wiki_article(term)
    await interaction.response.send_message("Searching...", embed=wiki_embed())
    

async def main():
    await bot.tree.sync()
    
bot.run(TOKEN)
