# imagedatabasebot
Discord image- stores images locally in the same folder as py script &amp; sends images from the local folder when a command is used.

This is a bot that stores ALL images that meet the image criteria locally on the machine from discord servers the bot has access to. It only downloads: '.png', '.jpeg', '.jpg', and '.gif' for security reasons (i.e no executables or other malicious software that could potentially be spread). Additonally, the image requirements stop the python script &amp; other bot files from being sent as they are hosted in the same folder.

Several changes are REQUIRED to be made by the user: log files outputs (if you want log name customization), directory needs to be added for image downloading (needs to be the same folder as the other bot files), along with discord bot ID to filter its own messages and the required token to link the bot to the script.

This code is free to be used, modified, and distributed by anyone.

If you have any additional questions feel free to dm me on discord at: Joeyy#4628
