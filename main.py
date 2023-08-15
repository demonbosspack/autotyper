try:
    import os
    import discord
    from discord.ext import commands
    from colorama import Fore
    import time
    import tracemalloc
    import ctypes
    import threading
    import pystray
    from PIL import Image
except:
    os.system("python -m pip install pillow")
    os.system("python -m pip install pystray")
    os.system("python -m pip install discord.py-self")
    os.system("python -m pip install colorama")
    os.system("python -m pip install discord") 
tracemalloc.start()



bot = commands.Bot(command_prefix="$", self_bot=True)

@bot.event
async def on_ready():
    os.system("clear")
    print(f"                                                     {Fore.GREEN}Logged in!")
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Streaming(name="demon sefu tau", url="https://www.twitch.tv/#"))
    time.sleep(1.5)
    print( f"                      Username: {bot.user.name}#{bot.user.discriminator} | Id: {bot.user.id} | Servers: {len(bot.guilds)} | Friends: {len(bot.friends)}\n")
    


    
    
    
@bot.command()
async def start(ctx, msg_spam: str):
    await ctx.message.delete()
    while True:
        await ctx.send (msg_spam)
        time.sleep(3)



         
        
@bot.command()     
async def restart(ctx):
    id = str(ctx.author.id)
    if id == 'idu tau':
        await ctx.send('Shutting down the selfbot!')
        await ctx.bot.logout()
    else:
        await ctx.send("You dont have sufficient permmisions to perform this action!")


def minimize_to_tray(icon, item):
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def restore_from_tray(icon, item):
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
    ctypes.windll.user32.SetForegroundWindow(ctypes.windll.kernel32.GetConsoleWindow())


def login(tokenselected):
    bot.run(tokenselected, log_handler=None)


# Call the login function
login("tokenu tau")