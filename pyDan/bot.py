import discord
from discord import File
import os
client = discord.Client()

@client.event
async def on_ready():
    print("Ready!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$rules"):
        await message.channel.send(file=File("C:/Users/usuario/Desktop/server/rules.png"))

        await message.channel.send("**__MAKE SURE YOU FOLLOW ALL THE RULES OR SOMETHING BAD MIGHT HAPPEN TO YOU!__**\n"
                                   "\n"
                                   "@everyone\n"
                                   "\n"
                                   "**1)** Please, be respectful and polite to everyone here. If you're caught misbehaving, you will be punished uwu.\n"
                                   "\n"
                                   "**2)** Please don't spam to get attention. Tt can be bothersome for other people and they may want to leave :(.\n"
                                   "\n"
                                   "**3)** Please don't use the command @/everyone . Not like you can, but still, don't try it :eyes: . That is for mods and myself only. If you use it, there will be a price to pay uwu.\n"
                                   "\n"
                                   "**4)** Please keep private drama to yourselves. We don't want to get pulled into fights that arent for us uwu.\n"
                                   "\n"
                                   "**5)** Please don't DM people without permission on streams. Make sure to tell a mod and send them a screenshot if someone messages you without permission, or is making you feel uncomfortable.\n"
                                   "\n"
                                   "**6)** Please don't abuse swearing. Sometimes it's uncalled for and makes everyone uncomfortable... Plus it can be very rude so don't do it uwu.\n"
                                   "\n"
                                   "**7)** NO NSFW YA NASTIES.\n"
                                   "\n"
                                   "**8)** no cringe.")

    elif message.content.startswith("$info"):

        await message.channel.send(file=File("C:/Users/usuario/Desktop/server/servertitle.gif"))

        await message.channel.send("**__Welcome to Bunny Boop's server @everyone!__\n"
                                   "\n"
                                   "First, and most importantly, make sure you go check the <#801340817800429608> channel! It's important to follow the rules here or else you'll be punished uwu.\n"
                                   "\n"
                                   "If you'd like to have some cool roles, you can head to <#821549420616613931>. You'll find some roles for that little 'personal' touch!\n"
                                   "\n"
                                   "If you are new to the server, why not head towards <#801340587444797470>? There, you can give us a brief description about yourself and maybe even find someone that has your same likings! Give it a read!\n"
                                   "\n"
                                   "Thank you for coming into the server! I hope you have a fun time here!**")

        await message.channel.send(file=File("C:/Users/usuario/Desktop/server/socials.png"))

        await message.channel.send("**Follow me on twitch! https://twitch.tv/bunnyb00ps \n"
                                   "\n"
                                   "Follow me on instagram! https://instagram.com/bunnyb00ps/ \n"
                                   "\n"
                                   "Follow me on tiktok: https://tiktok.com/@bunnyb00psy**")

        await message.channel.send(file=File("C:/Users/usuario/Desktop/server/channels.png"))

    elif message.content.startswith("$-info2"):
        await message.channel.send("**<#801340184847056896> - This channel is for the welcome cards!\n"
                                   "\n"
                                   "<#834287148219236372> - You're here right now. This channel contains important information about the server!\n"
                                   "\n"
                                   "<#801340817800429608> - The rules of the server! Very interesting channel, you should check it out!\n"
                                   "\n"
                                   "<#821549420616613931> - This channel's only purpose is to give you whatever role you want.\n"
                                   "\n"
                                   "<#834287090426576907> - In this channel you'll find every single bot's command!\n"
                                   "\n"
                                   "<#822626488435736667> - Random polls from time to time!\n"
                                   "\n"
                                   "<#801676149763211324> - Where the mod's important message goes through. Also something that you gotta check out!\n"
                                   "\n"
                                   "<#834302442362634240> - Whenever mom decides to stream (that'll be in a long time), the notification will pop here!**")
        await(message.channel.send("**<#816026252523339788> - Dad uploads some funny memes here, but he doesn't upload daily...\n"
                                   "\n"
                                   "<#803811628453855263> - Where people make fun of mom, I don't participate here... ~~only sometimes~~\n"
                                   "\n"
                                   "<#801340362416717834> - The main chat! Where the magic happens...\n"
                                   "\n"
                                   "<#821580363431673907> - Hey gamer, this is the chat for you.\n"
                                   "\n"
                                   "<#801340184847056897> - Whenever mom makes something funny or silly, you can clip it and post it here!\n"
                                   "\n"
                                   "<#804993725633134592> - Here you have mom's quotes... some of them are... weird nonetheless.\n"
                                   "\n"
                                   "<#801340534396289035> - You can show us your pretty face here!\n"
                                   "\n"
                                   "<#801340627416776704> - Pretty self explanatory ain't it.\n"
                                   "\n"
                                   "<#801340798624727070> - If you want mom to do/play something, here's the chat to suggest it! Though I wouldn't recommend suggesting 'stream more'. \n"
                                   "\n"
                                   "<#801695278134460426> - Your cute pets go right in here. We separate them from human beings because pets are cute on their own special and wholesome way\n"
                                   "\n"
                                   "<#801695697547427870> - You can send youtube links, soundcloud- hell, you can even promote yourself here!\n"
                                   "\n"
                                   "<#815519757402636310> - If you like art, then you should go in here. If you make art, you should also go in here. Share us your artwork!\n"
                                   "\n"
                                   "<#801693487619244102> - Ah yes, where the spam happens. Here you can use bots (But you can't use me... Dad doesn't want me playing around with strangers...)\n"
                                   "\n"
                                   "<#801680827314077716> - The spamming capsule. Make sure to always mute this chat! You never know when someone will decide to binge play with this bot.\n"
                                   "\n"
                                   "The :crown: Admin Suite is where mom and dad hang out. They're there from time to time and share things. They told me not to talk about them but I don't even understand it.\n"
                                   "\n"
                                   "<#821580557254787082> - This channel is where you talk if you don't have a microphone or are too shy to talk to others (it's ok, I've been there too). Only if you're in the 'Lobby' voice chat.\n"
                                   "\n"
                                   "<#821580627399671828> - Same thing as before, but in this case, for the 'gamies' voice chat!**"))

        await message.channel.send(file=File("C:/Users/usuario/Desktop/server/_spacer.png"))

        await message.channel.send("https://discord.gg/xTRUKRwbF3")

        await message.channel.send(file=File("C:/Users/usuario/Desktop/server/_spacer.png"))



    elif message.content.startswith("$b"):
        await message.channel.send("Stooop~")

    elif message.content.startswith("$parents"):
        await message.channel.send("My parents are <@252564881360814080> and <@395813023866159108>. I love them so much!")

    elif message.content.startswith("$otinf"):
        await message.channel.send(file=File("C:/Users/usuario/Desktop/server/howto.png"))

        await message.channel.send("***__ALL THE BOTS CONTAIN THEIR PREFIX ON THE BEGINNING OF THEIR NAME!__***\n"
                                   "\n"
                                   "Here's a brief explanation on what they do:\n"
                                   "\n"
                                   "<@159985870458322944> is our moderation bot! It keeps things clean!\n"
                                   "\n"
                                   "<@375805687529209857> This bot tells us when mom goes live!\n"
                                   "\n"
                                   "<@438057969251254293> allows you to play pokemon in a very much realistic way!\n"
                                   "\n"
                                   "<@235148962103951360> is the one who hands out the roles!\n"
                                   "\n"
                                   "<@440996323156819968> is our welcomer bot! He says hi to everyone who dares to step into my mom and dad's lair!\n"
                                   "\n"
                                   "<@746935716591960194> is me! Hi!\n"
                                   "\n"
                                   "<@  239631525350604801> is a currency bot for those who are into economy bots! You can collect pancakes and then... collect more pancakes with those pancakes!\n"
                                   "\n"
                                   "To be continued? D:")

client.run("NzQ2OTM1NzE2NTkxOTYwMTk0.X0HkGA.GH8l_wrHfM-yfH0xiZ_35OsVK78")
