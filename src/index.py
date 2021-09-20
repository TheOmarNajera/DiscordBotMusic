import discord
from discord.ext import commands
from decouple import config
import datetime
from urllib import parse, request
import re, os
import youtube_dl

token = str(config('bot_token'))

bot = commands.Bot(command_prefix='!',description="This is a helper bot")

def youtube(search):
    print(search)
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    url = 'https://www.youtube.com/watch?v=' + search_results[0]
    return url

@bot.command()
async def play(ctx,*,url):
    song_there = os.path.isfile("song.mp3")
    print(url)
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice:
        pass
    else:
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=str(ctx.author.voice.channel))
        await voiceChannel.connect()
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '200',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        patron = r"(https:\/\/www\.youtube\.com\/watch\?v=(\S{11}))"
        if re.match(patron,url):
            pass
        else:
            url = youtube(url)

        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

@bot.command()
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

@bot.command()
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")

@bot.command()
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")

@bot.command()
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice:
        voice.stop()
    else:
        await ctx.send("Currently no audio is playing.")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Información sobre el Servidor", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)

# Events
@bot.event
async def on_ready():
    print('My Bot is Ready')

bot.run(token)