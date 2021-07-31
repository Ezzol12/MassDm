import discord
from discord.ext import commands
import os
import threading
import requests
import urllib.request
import json
import asyncio
import colorama
import time
import sys
from colorama import Fore

user = "root"
password = "root"

print(f"""

{Fore.MAGENTA}  ___  ___           _             
{Fore.MAGENTA} | . || | '___ ._ _ | |__ ___  _ _ 
{Fore.MAGENTA} | | || |-<_> || ' || / /<_> || '_>
{Fore.MAGENTA} `___'|_| <___||_|_||_\_\<___||_|  
                                  

""")

usercheck = input(f"{Fore.RED} user >> ")
passwordcheck = input(f"{Fore.MAGENTA} {usercheck} password >> ")

os.system('cls')

message = "Checking..."

print(f"""

{Fore.MAGENTA}  ___  ___           _             
{Fore.MAGENTA} | . || | '___ ._ _ | |__ ___  _ _ 
{Fore.MAGENTA} | | || |-<_> || ' || / /<_> || '_>
{Fore.MAGENTA} `___'|_| <___||_|_||_\_\<___||_|  
                                  

""")

for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.4)


if user == usercheck:
    if passwordcheck == password:
        pass
    else:
        while True:
            pass
else:
    while True:
        pass

os.system('cls')

print(f"""

{Fore.MAGENTA}  ___  ___           _             
{Fore.MAGENTA} | . || | '___ ._ _ | |__ ___  _ _ 
{Fore.MAGENTA} | | || |-<_> || ' || / /<_> || '_>
{Fore.MAGENTA} `___'|_| <___||_|_||_\_\<___||_|  
                                  

""")

message2 = "Login Success!"

os.system('cls')

for char in message2:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.3)

time.sleep(3)

os.system("cls")

print(f"""

{Fore.MAGENTA}  ___  ___           _             
{Fore.MAGENTA} | . || | '___ ._ _ | |__ ___  _ _ 
{Fore.MAGENTA} | | || |-<_> || ' || / /<_> || '_>
{Fore.MAGENTA} `___'|_| <___||_|_||_\_\<___||_|  
                                  

""")

client = discord.Client()

token2 = input(f"{Fore.RED}(i putted it in my file because i put blank this) Input Token >>")

@client.event
async def on_connect():

    g = input("what do u want to send >> ")

    for user in client.user.friends:
        try:
            await user.send(g)
            print(f"message sent to: {user.name}")
        except:
            print(f"cannot sent messaged to : {user.name}")

client.run("ODU0MzYyNDI4OTU4OTY1ODAw.YQKFog.ETLCCj3JX79co3Q9P4K1KwlqSj0", bot = False)
