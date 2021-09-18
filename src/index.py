import discord
from discord.ext import commands
from decouple import config
import datetime

token = str(config('bot_token'))

bot = commands.Bot(command_prefix='>',description="This is a helper bot")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem impsum asdasd", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    print(f"{ctx.guild.icon}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)

# Events
@bot.event
async def on_ready():
    print('My Bot is Ready')

bot.run(token)