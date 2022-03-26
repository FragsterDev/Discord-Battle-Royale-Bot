import discord
from discord.ext import commands
import os

prefix = "]]"

intents = discord.Intents(messages=True, guilds=True)
client = commands.Bot(command_prefix=prefix, intents=intents)


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency,3)*1000}ms')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")
        print(f"Successfully loaded {filename}\n")


@client.command()
async def load(ctx, extension):
    if ctx.author.id == 505814544002842644:
        client.load_extension(f"cogs.{extension}")
        await ctx.send(f"Loaded {extension}")
    else:
        await ctx.send("Only bot owners have the permission to use this.")

@client.command()
async def unload(ctx, extension):
    if ctx.author.id == 505814544002842644:
        client.unload_extension(f"cogs.{extension}")
        await ctx.send(f"Unloaded {extension}")
    else:
        await ctx.send("Only bot owners have the permission to use this.")

@client.command()
async def reload(ctx, extension):
    if ctx.author.id == 505814544002842644:
        client.reload_extension(f"cogs.{extension}")
        await ctx.send(f"Reloaded {extension}")
    else:
        await ctx.send("Only bot owners have the permission to use this.")



client.run("OTAwMjYyNjU5NjM3Nzk2OTI0.YW-w8A.cGSjLIVMxwYWPH59K4VP6JJdyc0")