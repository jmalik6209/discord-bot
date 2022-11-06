import discord
from discord.ext import commands
import random

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun Commands Ready!")
    
    @commands.command()
    async def magic8ball(self, ctx, *, question):
        ballresponses = ['Yes', 'No', 'It is certain', 'It is decidedly so', 'Without a doubt', 'Yes - definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Affirmative', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(ballresponses)}")
    
    @commands.command()
    async def rps_rock(self, ctx):
        user_choice = "rock"
        bot_choice = random.choice(["rock", "paper", "scissors"])
        if bot_choice == user_choice:
            await ctx.send("It's a tie!")
        elif bot_choice == "paper":
            await ctx.send("YES! I win! Paper beats rock!")
        elif bot_choice == "scissors":
            await ctx.send("NOOOO! You win! Rock beats scissors!")
    
    @commands.command()
    async def rps_paper(self, ctx):
        user_choice = "paper"
        bot_choice = random.choice(["rock", "paper", "scissors"])
        if bot_choice == user_choice:
            await ctx.send("It's a tie!")
        elif bot_choice == "scissors":
            await ctx.send("YES! I win! Scissors beats paper!")
        elif bot_choice == "rock":
            await ctx.send("NOOOO! You win! Paper beats rock!")
    
    @commands.command()
    async def rps_scissors(self, ctx):
        user_choice = "scissors"
        bot_choice = random.choice(["rock", "paper", "scissors"])
        if bot_choice == user_choice:
            await ctx.send("It's a tie!")
        elif bot_choice == "rock":
            await ctx.send("YES! I win! Rock beats scissors!")
        elif bot_choice == "paper":
            await ctx.send("NOOOO! You win! Scissors beats paper!")

    @commands.command()
    async def flip(self, ctx):
        choice = random.choice(["heads", "tails"])
        if choice == "heads":
            await ctx.send("It's heads!")
        elif choice == "tails":
            await ctx.send("It's tails!")
    
    @commands.command()
    async def say(self, ctx, *, message):
        await ctx.send(message)
    
    @commands.command()
    async def sayembed(self, ctx, *, message):
        await ctx.send(embed=discord.Embed(description=message))

    @commands.command()
    async def diceroll(self, ctx):
        dice = random.randint(1, 6)
        await ctx.send(f"You rolled a {dice}!")

async def setup(bot):
    await bot.add_cog(fun(bot))