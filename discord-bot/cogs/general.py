import requests, json, io, random
import discord
from discord.ext import commands

class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("General Commands Ready!")
    
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hey There! To get a menu of the various commands, type $help")
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")
        
    @commands.command()
    async def random_image(self, ctx):
        response = requests.get("https://picsum.photos/200/300")
        img = io.BytesIO(response.content)
        await ctx.send(file=discord.File(img, filename="random.png"))
    
    @commands.command()
    async def inspire(self, ctx):
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" + json_data[0]['a']
        e = discord.Embed(title="Inspiring Quote", description=quote)
        await ctx.send(embed=e)
    
    @commands.command()
    async def qrcode(self, ctx, *, text):
        url = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={text}"
        response = requests.get(url)
        img = io.BytesIO(response.content)
        await ctx.send(file=discord.File(img, filename="qrcode.png"))
    
    @commands.command()
    async def pwgen(self, ctx, numbers, letters, symbols):
        try:
            numbers = int(numbers)
            letters = int(letters)
            symbols = int(symbols)
            numberslist = [
                "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
                ]
            letterslist = [
                "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
            ]
            symbolslist = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", ":", ";", "\"", "'", ",", "<", ".", ">", "/", "?"]
            password = ""

            for i in range(numbers):
                password += random.choice(numberslist)
            for i in range(letters):
                password += random.choice(letterslist)
            for i in range(symbols):
                password += random.choice(symbolslist)
            
            await ctx.author.send(password)
            await ctx.send("Password sent to your DMs!")
        except:
            await ctx.send("Invalid command, please use `$pwgen <numbers> <letters> <symbols>`")

async def setup(bot):
    await bot.add_cog(general(bot))