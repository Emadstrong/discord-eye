from os import system
import psutil
import time
import sys
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone
from dotenv import load_dotenv

load_dotenv()
bot_token = os.environ['bot_token'] 

mytitle = "Developed by @ureload / @0x892"
system("title "+mytitle)

client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.MAGENTA}
⠀⠀⠀⠀⠀⠀

{Style.RESET_ALL}
                                              {Fore.CYAN}   Owner : Unknown.{Style.RESET_ALL}
        """)
token = input(f'bot_token')
input_guild_id = input('1188399194751373362')
output_guild_id = input('1205804578826887228')

print(" ii ")
print("  gg")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Вход с аккаунта : {client.user}")
    print("Клонирование началось")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.BLUE}
⠀⠀⠀⠀⠀⠀⠀⠀⠀

THE END!
    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    await client.close()


client.run(bot_token)
