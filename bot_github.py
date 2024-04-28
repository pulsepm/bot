import requests
import git

import discord

def wiki_article(article: str) -> None:
    url = f"https://github.com/pulsepm/pulse/wiki/{str(article)}"
    response = requests.get(url)
    print(url)
    if response.status_code == 200:
        print(f"The wiki page '{article}' exists.")
    elif response.status_code == 404:
        print(f"The wiki page '{article}' does not exist.")
    else:
        print(f"Failed to check the existence of the wiki page. Status code: {response.status_code}")


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
