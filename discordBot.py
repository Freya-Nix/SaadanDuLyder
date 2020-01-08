import discord
import discordBot

TOKEN = 'NjY0MzcyMzE0MDI0MDUwNjg4.XhWIGQ.t5068VJ62W2KqXMJAUUgmub2lBQ'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

client.run(TOKEN)
