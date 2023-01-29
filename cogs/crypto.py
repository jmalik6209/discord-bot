from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
import discord
from discord.ext import commands

all_coins_list = [
    'bitcoin', 
    'ethereum', 
    'litecoin', 
    'ripple', 
    'stellar', 
    'monero', 
    'nem', 
    'cardano', 
    'verge', 
    'dash', 
    'dogecoin', 
    'bitcoin-cash', 
    'ethereum-classic',
    'shiba-inu',
    'iota',
    ]

class crypto(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Crypto Commands Ready!")
    
    @commands.command()
    async def btc(self, ctx):
        data = cg.get_price(ids = 'bitcoin', vs_currencies = 'usd')
        await ctx.send(f"Bitcoin price: **${data['bitcoin']['usd']}**")

    @commands.command()
    async def eth(self, ctx):
        data = cg.get_price(ids = 'ethereum', vs_currencies = 'usd')
        await ctx.send(f"Ethereum price: **${data['ethereum']['usd']}**")
    
    @commands.command()
    async def ltc(self, ctx):
        data = cg.get_price(ids = 'litecoin', vs_currencies = 'usd')
        await ctx.send(f"Litecoin price: **${data['litecoin']['usd']}**")
    
    @commands.command()
    async def xrp(self, ctx):
        data = cg.get_price(ids = 'ripple', vs_currencies = 'usd')
        await ctx.send(f"Ripple price: **${data['ripple']['usd']}**")
    
    @commands.command()
    async def xlm(self, ctx):
        data = cg.get_price(ids = 'stellar', vs_currencies = 'usd')
        await ctx.send(f"Stellar price: **${data['stellar']['usd']}**")
    
    @commands.command()
    async def xmr(self, ctx):
        data = cg.get_price(ids = 'monero', vs_currencies = 'usd')
        await ctx.send(f"Monero price: **${data['monero']['usd']}**")
    
    @commands.command()
    async def xem(self, ctx):
        data = cg.get_price(ids = 'nem', vs_currencies = 'usd')
        await ctx.send(f"NEM price: **${data['nem']['usd']}**")
    
    @commands.command()
    async def ada(self, ctx):
        data = cg.get_price(ids = 'cardano', vs_currencies = 'usd')
        await ctx.send(f"Cardano price: **${data['cardano']['usd']}**")
    
    @commands.command()
    async def xvg(self, ctx):
        data = cg.get_price(ids = 'verge', vs_currencies = 'usd')
        await ctx.send(f"Verge price: **${data['verge']['usd']}**")
    
    @commands.command()
    async def dash(self, ctx):
        data = cg.get_price(ids = 'dash', vs_currencies = 'usd')
        await ctx.send(f"Dash price: **${data['dash']['usd']}**")
    
    @commands.command()
    async def doge(self, ctx):
        data = cg.get_price(ids = 'dogecoin', vs_currencies = 'usd')
        await ctx.send(f"Dogecoin price: **${data['dogecoin']['usd']}**")
    
    @commands.command()
    async def bch(self, ctx):
        data = cg.get_price(ids = 'bitcoin-cash', vs_currencies = 'usd')
        await ctx.send(f"Bitcoin Cash price: **${data['bitcoin-cash']['usd']}**") 
    
    @commands.command()
    async def etc(self, ctx):
        data = cg.get_price(ids = 'ethereum-classic', vs_currencies = 'usd')
        await ctx.send(f"Ethereum Classic price: **${data['ethereum-classic']['usd']}**")

    @commands.command()
    async def shiba_inu(self, ctx):
        data = cg.get_price(ids = 'shiba-inu', vs_currencies = 'usd')
        await ctx.send(f"Shiba Inu price: **${data['shiba-inu']['usd']}**")\
    
    @commands.command()
    async def iota(self, ctx):
        data = cg.get_price(ids = 'iota', vs_currencies = 'usd')
        await ctx.send(f"IOTA price: **${data['iota']['usd']}**")
    
    @commands.command()
    async def allcrypto(self, ctx):
        embed = discord.Embed(
            title = "All Cryptocurrencies",
            description = "Prices for every crypto supported",
            color = discord.Color.blue()
        )
        for i in all_coins_list:
            data = cg.get_price(ids = i, vs_currencies = 'usd')
            embed.add_field(name = i, value = f"**${data[i]['usd']}**", inline = False)
        await ctx.send(embed = embed)


async def setup(bot):
    await bot.add_cog(crypto(bot))