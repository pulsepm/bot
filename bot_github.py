import requests
import git

import discord

def wiki_article(article: str) -> bool:
  """Checks if a GitHub wiki page exists using HEAD request.

  Args:
      url (str): The URL of the GitHub wiki page.

  Returns:
      bool: True if the page exists, False otherwise.
  """
  headers = {'Accept': 'application/json'} 
  response = requests.head(f"https://github.com/pulsepm/pulse/wiki/{article}", headers=headers)
  return response.status_code == 200

def wiki_embed():
    embed = discord.Embed(
        title="Pulse Wikipedia",
        description="This is our best results so far.",
        color=discord.Color.dark_red()
    )
    embed.set_author(name="Pulse")
    embed.add_field(name="Field 1", value="Value 1", inline=False)
    embed.add_field(name="Field 2", value="Value 2", inline=False)
    embed.set_footer(text="Thanks for using Pulse")
    return embed
