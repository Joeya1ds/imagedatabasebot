import discord
import os
import random
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix='.')
image_types = ["png", "jpeg", "jpg", "gif"] #accepted image types

@client.event
async def on_ready():
    print("Bot is ready.")


@client.event
async def on_message(message):
    username = message.author.name
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})') #logs tracked messages in the console

    for attachment in message.attachments: #downloads images from discord server using supported file types
        if any(attachment.filename.endswith(image) for image in image_types):
            await attachment.save(attachment.filename)
        return

    if user_message.lower() == '!image': #pulls images from listed directory
        filename = random.choice(os.listdir('')) #paste image directory here (will likely be the same as py script)
        if any(filename.lower().endswith(image) for image in image_types):
            await message.channel.send(file=discord.File(filename))
            return
        else:
            await message.channel.send("Error in sending attachment, attachment file type not supported. Try again.") #Error for if py script is attempted to be sent instead of image
            return


client.run('') #paste the discord bot token here