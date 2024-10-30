import discord
import os
from discord.ext import commands


class DiscordBot(commands.Bot):
    def __init__(self):        
        super(DiscordBot, self).__init__(command_prefix='!', case_insensitive=True, intents=discord.Intents.all())

        @self.event
        async def on_ready():
            print("KhoBot ready for action!")

    async def load(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")
    
    def get_token(self):
        __token_file = open('token.txt')
        __token = __token_file.read()
        return __token
    
