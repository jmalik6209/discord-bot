import discord
from discord.ext import commands
import random
import json
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


class math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Math Commands Ready!")
    
    @commands.command()
    async def calculate(self, ctx, *, equation):
        try:
            await ctx.send(eval(equation))
        
        except:
            await ctx.send('''
            Sorry, I can't calculate that. Please use the following format for calculations:
Symbol:   |   Operation:
-----------------------------
+               |   Addition
-                |   Subtraction
*                |   Multiplication
/               |   Division
**              |   To the power of (Exponents)
() or []     |   Parentheses or Brackets
            ''')

    @commands.command()
    async def randomgraph(self, ctx):
        xpoint_1 = random.randint(0,100)
        xpoint_2 = random.randint(0,100)
        ypoint_1 = random.randint(0,100)
        ypoint_2 = random.randint(0,100)

        await ctx.send(f'''Points: 
X Start:{xpoint_1}, 
X End: {xpoint_2}, 
Y Start: {ypoint_1}, 
Y End: {ypoint_2}''')
        xpoints = np.array([xpoint_1, xpoint_2])
        ypoints = np.array([ypoint_1, ypoint_2])
        colors = [
            "blue",
            "red",
            "green",
            "yellow",
            "cyan",
            "magenta",
            "black",
        ]
        plt.plot(xpoints, ypoints, color=random.choice(colors))
        plt.savefig("plot.png")
        await ctx.send(file=discord.File(open("plot.png", "rb"), filename="plot.png"))
        plt.clf()
    
    @commands.command()
    async def plot(self, ctx, arg1, arg2, arg3, arg4):
        try:
            x1 = float(arg1)
            x2 = float(arg2)
            y1 = float(arg3)
            y2 = float(arg4)
            x = np.array([x1, x2])
            y = np.array([y1, y2])
            colors = [
                "blue",
                "red",
                "green",
                "yellow",
                "cyan",
                "magenta",
                "black",
            ]

            plt.plot(x, y, color=random.choice(colors))
            plt.grid()
            plt.xlabel("X Axis")
            plt.ylabel("Y Axis")
            plt.title("Plot")
            plt.savefig("plot.png")
            await ctx.send(f"Points:\n X Start: {x1}\n X End: {x2}\n Y Start: {y1}\n Y End: {y2}")
            await ctx.send(file=discord.File(open("plot.png", "rb"), filename="plot.png"))
            plt.clf()

        except:
            await ctx.send("Invalid Input - please try again!")
            plt.clf()


async def setup(bot):
    await bot.add_cog(math(bot))