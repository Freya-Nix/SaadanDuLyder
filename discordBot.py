import discord
import os
from dotenv import load_dotenv
import capitalization

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} has connected to Discord\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    copy = message.content
    print(message.content)
    print(message.author)
    await message.channel.send('"{}" det er sådan du lyder.'.format(capitalization.randomCap(copy)))

@client.event
async def on_message_edit(before, message):
    await message.channel.send("(redigeret)")
    print(f'{before}')

client.run(TOKEN)
