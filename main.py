import discord, random, json, os, asyncio
from discord.ext import commands
"""
Basically a big meme of a discord bot
TODO:
    Implement source control -high priority 3/29
    wrtie logic for kick command that determines if user is present or not
    more memes
"""
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents, case_insensitive=True)
with open(r'D:\PyProjects\Discordbot\Discordbot2\config.json') as x:
    data = json.load(x)
    token = data["token"]
    paul = data["paul"]
    zkills = data["zkills"]
    groovy = data["groovy"]
    serverid = data["guild"]
    invlink = data["invlink"]
    
    
@bot.event
async def on_ready():
    print('badmin bot is ready')
    game = discord.Game('dude weed')
    await bot.change_presence(activity=game)
 
cmdamt = 0    #janky way to store amount of kick commands for now

@bot.command() #may need to set a few aliases in order to account for nonsober command passes if case_insensitive doesn't work
@commands.has_permissions(kick_members=True)
async def kick(ctx, reason=None):
    
        #Get member objects here, then pass kick to those objects after if/then statement
    guild = bot.get_guild(int(serverid))
    guild_members = [
        guild.get_member(int(paul)),
        guild.get_member(int(zkills))
    ]

    await ctx.send("A thousand words...")
    number = random.randrange(1488)
    rekt = random.choice(guild_members)
    if number == 69:
        await ctx.send('Rolled number' + ' ' + str(number))
        await ctx.send(file=discord.File('D:/PyProjects/DiscordBot/Discordbot2/img/kick/nuked.gif'))
        await asyncio.sleep(3)
        await ctx.send('kicking' + ' ' + str(rekt))
        await rekt.send(invlink)
        await rekt.kick()
        
    elif number == 420:
        await ctx.send('Rolled number' + ' ' + str(number))
        await ctx.send('dude weed')
    elif number == 1488:
        await ctx.send('Rolled number' + ' ' + str(number))
        await ctx.send('fuck i did this while i high')
    else:

        await ctx.send('Rolled number' + ' ' + str(number))
    
    def increment(): #janky way to increment amount of kick attempts
        global cmdamt
        cmdamt += 1
    increment()
    if cmdamt == 100:
        await ctx.send('100 unsuccesful kick attempts!')
    elif cmdamt == 1000:
        await ctx.send('1000 fucking unsuccesful kick attempts wtf')
    elif cmdamt == 2000:
        await ctx.send('fuck it, kicking someone')
        await rekt.send(invlink)
        await rekt.kick()
        cmdamt == 0
    else:
        pass
    command_amounts = {
    'attempts' : cmdamt
    }
    with open('amtofcmmds.json', 'w') as cmd_dump:
        json.dump(command_amounts, cmd_dump)
    print('Kick has been called' + ' ' + str(cmdamt) + ' ' + 'times!')

    #todo: need to add in response for whenever member object returns none

@bot.event
async def on_message(message):
    paulpath = random.choice(os.listdir(r'D:\PyProjects\DiscordBot\DiscordBot2\img\paul'))
    zkpath = random.choice(os.listdir("D:/PyProjects/Discordbot/Discordbot2/img/zkills"))

    if 'paul' in message.content:
        await message.channel.send(file=discord.File('D:/PyProjects/Discordbot/DiscordBot2/img/paul/' + paulpath))
    elif 'zkills' in message.content:
        await message.channel.send(file=discord.File('D:/PyProjects/Discordbot/Discordbot2/img/zkills/' + zkpath))
    await bot.process_commands(message)


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.channel.send("nope")
    elif isinstance(error, AttributeError):
        await ctx.channel.send("no one left boss")


bot.run(token)