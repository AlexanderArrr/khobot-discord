import asyncio
from discordbot import DiscordBot

discord_bot = DiscordBot()

async def main():
    async with discord_bot:
        await discord_bot.load()
        await discord_bot.start(discord_bot.get_token())

asyncio.run(main())

