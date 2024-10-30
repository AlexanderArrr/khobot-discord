import discord
from discord.ext import commands

class MessageCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot_channel = None
        self.announce_channel = None

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Cog {__name__} successfully added!")

    @commands.command()
    async def echo(self, ctx, *, arg):
        if self.bot_channel is None:
            await ctx.send(embed=discord.Embed(title='Error!', 
                                               description="No bot channel has been set!\nPlease use the '!setup_bot' command in your desired bot channel."))
        else:
            await self.bot_channel.send(embed=discord.Embed(title='Echo', description=arg))

    @commands.command()
    async def ping(self, ctx):
        await self.bot_channel.send('Pong')

    @commands.command()
    async def channel_id(self, ctx):
        if not ctx.author.roles[-1].permissions.administrator:
            await ctx.send(embed=discord.Embed(title="ACCESS DENIED", 
                                               description=f"You do not have the required admin permissions to use this command!"))
            return
        await self.bot_channel.send(f"The channel **{ctx.channel.name}** has the ID **{ctx.channel.id}**")

    @commands.command()
    async def setup_bot(self, ctx):
        if not ctx.author.roles[-1].permissions.administrator:
            await ctx.send(embed=discord.Embed(title="ACCESS DENIED", 
                                               description=f"You do not have the required admin permissions to use this command!"))
            return
        self.bot_channel = ctx.channel
        await self.bot_channel.send(embed=discord.Embed(title="SUCCESS", 
                                                        description=f"The channel **{self.bot_channel.name}** has been set as the bot channel!"))

    @commands.command()
    async def setup_announce(self, ctx):
        if not ctx.author.roles[-1].permissions.administrator:
            await ctx.send(embed=discord.Embed(title="ACCESS DENIED", 
                                               description=f"You do not have the required admin permissions to use this command!"))
            return
        self.announce_channel = ctx.channel
        await self.announce_channel.send(embed=discord.Embed(type="SUCCESS", 
                                                             description=f"The channel **{self.announce_channel.name}** has been set as the announcement channel!"))

async def setup(bot):
    await bot.add_cog(MessageCommands(bot))