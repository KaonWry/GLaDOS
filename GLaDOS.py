#
# Code Written by JustATac0
#

import discord
import time
import asyncio
import os
from dotenv import load_dotenv
from discord.ext import commands,tasks
from time import sleep
from discord import FFmpegPCMAudio
from discord.utils import get

load_dotenv()

client = commands.Bot(command_prefix = ['-', 'GLaD '])
TOKEN = os.getenv("DISCORD_TOKEN")

    
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Portal"))
    print(f"Logged in as {client.user.name}({client.user.id})")

@client.command()
async def join(ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        return await ctx.send("Please return to the Aperture Science computer-aided enrichment center.")
    if not ctx.author.voice:
       return await ctx.send("Did you really think that would work if you weren't connected to a voice channel?")
    channel = ctx.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        await channel.connect()
    client_channel = ctx.voice_client.channel
    if channel and channel == client_channel:
        if voice and voice.is_connected():
            await ctx.send("I'm already in the voice channel with you.")

@client.command()
async def leave(ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        return await ctx.send("Please return to the Aperture Science computer-aided enrichment center.")
    if not ctx.message.guild.voice_client:
       return await ctx.send("I'm not currently connected to any voice channels.", delete_after = 5.0)
    await ctx.voice_client.disconnect()

@client.command()
async def stillalive(ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        return await ctx.send("Please return to the Aperture Science computer-aided enrichment center.")
    if not ctx.author.voice:
        return await ctx.send("Did you really think that would work if you weren't connected to a voice channel?")
    channel = ctx.author.voice.channel
    if not channel:
        return await ctx.send("Did you really think that would work if you weren't connected to a voice channel?")
    voice = get(client.voice_clients, guild=ctx.guild)
    if not voice:
        await ctx.send("Did you really think that would work if I wasn't connected to a voice channel?")
    if voice and voice.is_playing():
        return await ctx.send("Please wait until I am finished before using another voice channel command.")
    if voice and voice.is_connected():
        async with ctx.typing():
            await asyncio.sleep(3)
        await ctx.send("This was a triumph.")
        await voice.move_to(channel)
        source = FFmpegPCMAudio('stillalive.mp3')
        player = voice.play(source)
        async with ctx.typing():
            await asyncio.sleep(4)
        await ctx.send("I'm making a note here:")
        async with ctx.typing():
            await asyncio.sleep(1.5)
        await ctx.send("**HUGE SUCCESS.**")
        async with ctx.typing():
            await asyncio.sleep(3)
        await ctx.send("It's hard to overstate")
        async with ctx.typing():
            await asyncio.sleep(2)
        await ctx.send("my satisfaction.")
        async with ctx.typing():
            await asyncio.sleep(4.5)
        await ctx.send("Aperture Science")
        async with ctx.typing():
            await asyncio.sleep(4)
        await ctx.send("We do what we must")
        async with ctx.typing():
            await asyncio.sleep(1.5)
        await ctx.send("because we can.")
        async with ctx.typing():
            await asyncio.sleep(3)
        await ctx.send("For the good of all of us.")
        async with ctx.typing():
            await asyncio.sleep(3)
        await ctx.send("Except the ones who are dead.")
        async with ctx.typing():
            await asyncio.sleep(2)
        await ctx.send("But there's no sense crying")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("over every mistake.")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("You just keep on trying")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("till you run out of cake.")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("And the Science gets done.")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("And you make a neat gun.")
        async with ctx.typing():
            await asyncio.sleep(1.5)
        await ctx.send("For the people who are")
        async with ctx.typing():
            await asyncio.sleep(1.5)
        await ctx.send("**still alive.**")
        async with ctx.typing():
            await asyncio.sleep(8)
        await ctx.send("I'm not even angry.")
        async with ctx.typing():
            await asyncio.sleep(4)
        await ctx.send("I'm being so sincere right now.")
        async with ctx.typing():
            await asyncio.sleep(4)
        await ctx.send("Even though you")
        async with ctx.typing():
            await asyncio.sleep(2)
        await ctx.send("broke my heart.")
        async with ctx.typing():
            await asyncio.sleep(2)
        await ctx.send("And killed me.")
        async with ctx.typing():
            await asyncio.sleep(3)
        await ctx.send("And tore me to pieces.")
        async with ctx.typing():
            await asyncio.sleep(3)
        await ctx.send("And threw every piece into")
        async with ctx.typing():
            await asyncio.sleep(2.5)
        await ctx.send("a fire.")
        async with ctx.typing():
            await asyncio.sleep(3)
        await ctx.send("As they burned it hurt because")
        async with ctx.typing():
            await asyncio.sleep(3)
        await ctx.send("I was so happy for you!")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("Now these points of data")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("make a beautiful line.")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("And we're out of beta.")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("We're releasing on time.")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("So I'm GLaD. I got burned.")
        async with ctx.typing():
            await asyncio.sleep(1.5)
        await ctx.send("Think of all the things we learned")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("for the people who are")
        async with ctx.typing():
            await asyncio.sleep(1.2)
        await ctx.send("**still alive.**")
        async with ctx.typing():
            await asyncio.sleep(8)
        await ctx.send("Go ahead and leave me.")
        async with ctx.typing():
            await asyncio.sleep(4)
        await ctx.send("I think I prefer to stay inside.")
        async with ctx.typing():
            await asyncio.sleep(4)
        await ctx.send("Maybe you'll find")
        async with ctx.typing():
            await asyncio.sleep(2)
        await ctx.send("someone else")
        async with ctx.typing():
            await asyncio.sleep(2)
        await ctx.send("to help you.")
        async with ctx.typing():
            await asyncio.sleep(3)
        await ctx.send("Maybe Black Mesa")
        async with ctx.typing():
            await asyncio.sleep(3)
        await ctx.send("THAT WAS A JOKE.")
        async with ctx.typing():
            await asyncio.sleep(2)
        await ctx.send("** HA HA. FAT CHANCE.**")
        async with ctx.typing():
            await asyncio.sleep(2.5)
        await ctx.send("Anyway,")
        async with ctx.typing():
            await asyncio.sleep(1.5)
        await ctx.send("this cake is great.")
        async with ctx.typing():
            await asyncio.sleep(2)
        await ctx.send("It's so delicious and moist.")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("Look at me still talking")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("when there's Science to do.")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("When I look out there,")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("it makes me GLaD I'm not you.")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("I've experiments to run.")
        async with ctx.typing():
            await asyncio.sleep(1.5)
        await ctx.send("There is research to be done.")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("on the people who are")
        async with ctx.typing():
            await asyncio.sleep(1.2)
        await ctx.send("**still alive.**")
        async with ctx.typing():
            await asyncio.sleep(2)
        await ctx.send("And believe me I am")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("**still alive.**")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("I'm doing Science and I'm")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("**still alive.**")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("I feel FANTASTIC and I'm")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("**still alive.**")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("While you're dying I'll be")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("**still alive.**")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("And when you're dead I will be")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("**still alive.**")
        async with ctx.typing():
            await asyncio.sleep(1.5)
        await ctx.send("**STILL ALIVE**")
        async with ctx.typing():
            await asyncio.sleep(1.5)
        await ctx.send("**still alive.**")


@client.command()
async def wantyougone(ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        return await ctx.send("Please return to the Aperture Science computer-aided enrichment center.")
    if not ctx.author.voice:
        return await ctx.send("Did you really think that would work if you weren't connected to a voice channel?")
    channel = ctx.author.voice.channel
    if not channel:
        return await ctx.send("Did you really think that would work if you weren't connected to a voice channel?")
    voice = get(client.voice_clients, guild=ctx.guild)
    if not voice:
        await ctx.send("Did you really think that would work if I wasn't connected to a voice channel?")
    if voice and voice.is_playing():
        return await ctx.send("Please wait until I am finished before using another voice channel command.")
    if voice and voice.is_connected():
        await voice.move_to(channel)
        source = FFmpegPCMAudio('wantyougone.mp3')
        player = voice.play(source)
        async with ctx.typing():
            await asyncio.sleep(5)
        await ctx.send("Well here we are again")
        async with ctx.typing():
            await asyncio.sleep(1.5)
        await ctx.send("It's always such a pleasure")
        async with ctx.typing():
            await asyncio.sleep(2)
        await ctx.send("Remember when you tried")
        async with ctx.typing():
            await asyncio.sleep(1)
        await ctx.send("to kill me twice?")
        async with ctx.typing():
            await asyncio.sleep(2)
        await ctx.send("Oh how we laughed and laughed")
        async with ctx.typing():
            await asyncio.sleep(1.5)
        await ctx.send("Except I wasn't laughing")
        async with ctx.typing():
            await asyncio.sleep(2)
        await ctx.send("Under the circumstances")
        async with ctx.typing():
            await asyncio.sleep(1.5)
        await ctx.send("I've been shockingly nice")
        async with ctx.typing():
            await asyncio.sleep(3.2)
        await ctx.send("You want your freedom?")
        async with ctx.typing():
            await asyncio.sleep(1.5)
        await ctx.send("Take it")
        async with ctx.typing():
            await asyncio.sleep(2)
        await ctx.send("That's what I'm counting on")
        async with ctx.typing():
            await asyncio.sleep(4)
        await ctx.send("I used to want you dead")
        async with ctx.typing():
            await asyncio.sleep(2.3)
        await ctx.send("But")
        async with ctx.typing():
            await asyncio.sleep(0.05)
        await ctx.send("now I only want you gone")
        async with ctx.typing():
            await asyncio.sleep(6.8)
        await ctx.send("She was a lot like you")
        async with ctx.typing():
            await asyncio.sleep(1.6)
        await ctx.send("(Maybe not quite as heavy)")
        async with ctx.typing():
            await asyncio.sleep(1.4)
        await ctx.send("Now little Caroline is in here too")
        async with ctx.typing():
            await asyncio.sleep(3.5)
        await ctx.send("One day they woke me up")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("So I could live forever")
        async with ctx.typing():
            await asyncio.sleep(1.8)
        await ctx.send("It's such a shame the same")
        async with ctx.typing():
            await asyncio.sleep(0.8)
        await ctx.send("Will never happen to you")
        async with ctx.typing():
            await asyncio.sleep(3.8)
        await ctx.send("You've got your")
        async with ctx.typing():
            await asyncio.sleep(0.3)
        await ctx.send("short sad")
        async with ctx.typing():
            await asyncio.sleep(0.6)
        await ctx.send("life left")
        async with ctx.typing():
            await asyncio.sleep(2)
        await ctx.send("That's what I'm counting on")
        async with ctx.typing():
            await asyncio.sleep(4)
        await ctx.send("I'll let you get right to it")
        async with ctx.typing():
            await asyncio.sleep(2)
        await ctx.send("Now I only want you gone")
        async with ctx.typing():
            await asyncio.sleep(7.5)
        await ctx.send("Goodbye my only friend")
        async with ctx.typing():
            await asyncio.sleep(1.5)
        await ctx.send("Oh, did you think I meant you?")
        async with ctx.typing():
            await asyncio.sleep(1.5)
        await ctx.send("That would be funny")
        async with ctx.typing():
            await asyncio.sleep(1.5)
        await ctx.send("if it weren't so sad")
        async with ctx.typing():
            await asyncio.sleep(2.5)
        await ctx.send("Well you have been replaced")
        async with ctx.typing():
            await asyncio.sleep(1.5)
        await ctx.send("I don't need anyone now")
        async with ctx.typing():
            await asyncio.sleep(1.5)
        await ctx.send("When I delete you maybe")
        async with ctx.typing():
            await asyncio.sleep(1.5)
        await ctx.send("[REDACTED]")
        async with ctx.typing():
            await asyncio.sleep(2.6)
        await ctx.send("Go make some new disaster")
        async with ctx.typing():
            await asyncio.sleep(3.7)
        await ctx.send("That's what I'm counting on")
        async with ctx.typing():
            await asyncio.sleep(4.4)
        await ctx.send("You're someone else's problem")
        async with ctx.typing():
            await asyncio.sleep(2.7)
        await ctx.send("Now I only want you gone")
        async with ctx.typing():
            await asyncio.sleep(4)
        await ctx.send("Now I only want you gone")
        async with ctx.typing():
            await asyncio.sleep(4)
        await ctx.send("Now I only want you")
        async with ctx.typing():
            await asyncio.sleep(2.7)
        await ctx.send("gone")


@client.command(pass_context=True)
async def purge(ctx, amount=30):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount + 1):
              messages.append(message)

    await channel.delete_messages(messages)


client.run(TOKEN)