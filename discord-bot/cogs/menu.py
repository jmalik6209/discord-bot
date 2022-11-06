import discord
from discord.ext import commands

class menu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Menu Commands Ready!")
    
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Commands:", description="", color=0x206694)
        embed.add_field(name="$help", value="Shows this message.", inline=False)
        embed.add_field(name="$help_general", value="Shows General Commands", inline=False)
        embed.add_field(name="$help_crypto", value="Shows Crypto Commands", inline=False)
        embed.add_field(name="$help_fun", value="Shows Fun Commands", inline=False)
        embed.add_field(name="$help_math", value="Shows Math Commands", inline=False)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def help_general(self, ctx):
        embed = discord.Embed(title="General Commands:", description="", color=0x000000)
        embed.add_field(name="$hello", value="Bob the Bot greets you", inline=False)
        embed.add_field(name="$help", value="Lists all of the things Bob the Bot can do", inline=False)
        embed.add_field(name="$random_image", value="Bob the Bot will send you a random stock photo", inline=False)
        embed.add_field(name="$ping", value="You'll find out :)", inline=False)
        embed.add_field(name="$inspire", value="Bob the Bot gives you an inspiring quote", inline=False)
        embed.add_field(name="$qrcode [url]", value="Bob the Bot will generate a QR code for the url you specify", inline=False)
        embed.add_field(name="$pwgen [# of numbers] [# of letters] [# of symbols]", value="Bob the Bot will generate a random password", inline=False)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def help_crypto(self, ctx):
        embed = discord.Embed(title="Crypto Commands:", description="", color=0x000000)
        embed.add_field(name="$btc", value="Bob the Bot will send you the current price of Bitcoin", inline=False)
        embed.add_field(name="$eth", value="Bob the Bot will send you the current price of Ethereum", inline=False)
        embed.add_field(name="$ltc", value="Bob the Bot will send you the current price of Litecoin", inline=False)
        embed.add_field(name="$xrp", value="Bob the Bot will send you the current price of Ripple", inline=False)
        embed.add_field(name="$xlm", value="Bob the Bot will send you the current price of Stellar", inline=False)
        embed.add_field(name="$xmr", value="Bob the Bot will send you the current price of Monero", inline=False)
        embed.add_field(name="$xem", value="Bob the Bot will send you the current price of NEM", inline=False)
        embed.add_field(name="$ada", value="Bob the Bot will send you the current price of Cardano", inline=False)
        embed.add_field(name="$xvg", value="Bob the Bot will send you the current price of Verge", inline=False)
        embed.add_field(name="$dash", value="Bob the Bot will send you the current price of Dash", inline=False)
        embed.add_field(name="$doge", value="Bob the Bot will send you the current price of Dogecoin", inline=False)
        embed.add_field(name="$bch", value="Bob the Bot will send you the current price of Bitcoin Cash", inline=False)
        embed.add_field(name="$etc", value="Bob the Bot will send you the current price of Ethereum Classic", inline=False)
        embed.add_field(name="$shiba_inu", value="Bob the Bot will send you the current price of Shiba Inu", inline=False)
        embed.add_field(name="$allcrypto", value="Bob the Bot will send you the current price of all cryptocurrencies he supports", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def help_fun(self, ctx):
        embed = discord.Embed(title="Fun Commands:", description="", color=0x000000)
        embed.add_field(name="$magic8ball [YOUR QUESTION]", value="Bob the Bot will use his special magic 8 ball to give you a response to your question!", inline=False)
        embed.add_field(name="$rps_rock", value="Play Rock, Paper, Scissors with Bob the Bot with a choice of rock", inline=False)
        embed.add_field(name="$rps_paper", value="Play Rock, Paper, Scissors with Bob the Bot with a choice of paper", inline=False)
        embed.add_field(name="$rps_scissors", value="Play Rock, Paper, Scissors with Bob the Bot with a choice of scissors", inline=False)
        embed.add_field(name="$flip", value="Bob the Bot will flip a coin", inline=False)
        embed.add_field(name="$diceroll", value="Bob the Bot will roll a dice", inline=False)
        embed.add_field(name="$say [message]", value="Bob the Bot will say the message you want him to", inline=False)
        embed.add_field(name="$sayembed [message]", value="Bob the Bot will send an embed with the message you want him to", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def help_math(self, ctx):
        embed = discord.Embed(title="Math Commands:", description="", color=0x000000)
        embed.add_field(name = "$calculate [expression]", value = "Bob the Bot will calculate the expression you specify (no variables)", inline = False)
        embed.add_field(name  = "$randomgraph", value = "Bob the Bot will generate a random graph", inline = False)
        embed.add_field(name = "$plot [x start] [x end] [y start] [y end]", value = "Bob the Bot will plot a simple graph with the parameters you specify", inline = False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(menu(bot))
