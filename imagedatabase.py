import discord
import os
import random
from discord.ext import commands

print("Loading bot...")
client = commands.Bot(command_prefix='!')
image_types = ["png", "jpeg", "jpg", "gif"] #accepted image types

@client.event
async def on_ready():
    print("Loaded.")

@client.event
async def on_message(message):
    username = message.author.name
    user_message = str(message.content)
    channel = str(message.channel.name)
    userid = message.author.id

    chatfile = open('chatlog.txt', 'a') #tracks user chat logs in seperate file
    print(f'{userid}: {user_message} ({channel})', file=chatfile)
    chatfile.close()

    for attachment in message.attachments: #downloads images from discord server using supported file types
        if any(attachment.filename.endswith(image) for image in image_types):
            await attachment.save(attachment.filename)
            if userid != 886251876427890698: #Change to your bots userid, ignores bot messages in stored logs
                imgfile = open('imglog.txt', 'a') #logs user information for saved images
                print(f'Discord id {userid} sent an image {attachment.filename} in ({channel}) which was successfully saved!', file=imgfile)
                imgfile.close()
                return
        return

    if user_message.lower() == '!image': #pulls images from listed directory
        filename = random.choice(os.listdir('')) #paste image directory here (will likely be the same as py script). It needs to start with the driver letter with 2 forward slashes (i.e C:\\Users\\ExampleUser\..)
        if any(filename.lower().endswith(image) for image in image_types):
            await message.channel.send(file=discord.File(filename))
            return
        else:
            await message.channel.send("Error in sending attachment, attachment file type not supported. Try again.") #Error for if py script or logs are attempted to be sent instead of image
            return

    if user_message.lower() == '!help': #bot introduction
        imagenumber = (len(os.listdir()) - 1)
        await message.channel.send('Hello! This is _____, the image saving and sending bot. Images are automatically saved from any server the bot is added to. To recieve a random image run "!image". There are currently ' + str(imagenumber) + ' images saved across all servers!')
        return

client.run('') #paste the discord bot token here
