import discord
from discord.ext import commands
import json


class Channels(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def set_channel(self, ctx, channel_id):
        with open("channels.json","r") as f:
            channel = json.load(f)
        channel[str(ctx.guild.id)]=channel_id
        with open("channels.json", "w") as f:
            json.dump(channel,f)
        await ctx.send(f"The battle royale channel has been set to <#{channel_id}>")

    @commands.command()
    @commands.guild_only()
    async def channel(self,ctx):
        with open("channels.json", "r") as f:
            channel = json.load(f)
        if int(channel[str(ctx.guild.id)]) == 0:
            await ctx.send("No channel has been set up for the battle ground.\nUse `set_channel <channel_id>` to set it.")
        else:
            await ctx.send(f"The following channel is set as the battleground: <#{channel[str(ctx.guild.id)]}>.\nTo change the channel, use `set_channel <channel_id>`")


def setup(client):
    client.add_cog(Channels(client))
