import discord
from discord.ext import commands
import json


class Game(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def shoot(self,ctx,user: discord.Member):
        with open("channels.json", "r") as f:
            channel=json.load(f)
        with open("count.json", "r") as f:
            count=json.load(f)

        if channel[str(ctx.guild.id)] == 0:
            await ctx.send("The battle ground channel hasn't been set up yet."
                           "\nUse `set_channel <channel_id>` to set the battle ground channel.")

        if ctx.channel.id == int(channel[str(ctx.guild.id)]):
            prole = discord.utils.get(ctx.guild.roles,name="Player")
            srole = discord.utils.get(ctx.guild.roles,name="Spectator")
            if prole in user.roles:
                await user.add_roles(srole)
                await user.remove_roles(prole)
                c=count[str(ctx.guild.id)]
                c=c+1
                count[str(ctx.guild.id)]=c
                with open("count.json","w") as f:
                    json.dump(count,f)
                e=discord.Embed(color=discord.Colour.red())
                with open("count.json","r") as f:
                    count = json.load(f)
                e.add_field(name="Member Eliminated", value=f"{user.mention} was eliminated by {ctx.author.mention}",inline=False)
                e.add_field(name="Count",value=f"{user.mention} is the {count[str(ctx.guild.id)]}th member to be eliminated",inline=False)
                await ctx.send(embed=e)
            else:
                e=discord.Embed(color=discord.Colour.blue())
                e.add_field(name="Error",value="The user is already eliminated.",inline=False)
                await ctx.send(embed=e)
        else:
            e=discord.Embed(color=discord.Colour.orange())
            e.add_field(name="Alert",value=f"The game cannot be played outside <#{channel[str(ctx.guild.id)]}>",inline=False)
            await ctx.send(embed=e)

    @commands.command()
    @commands.guild_only()
    async def status(self,ctx):
        with open("count.json","r") as f:
            count=json.load(f)
        with open("channels.json","r") as f:
            channel=json.load(f)
        if count[str(ctx.guild.id)] !=0:
            e=discord.Embed(color=discord.Colour.orange())
            e.add_field(name="Status: Active",value=f"Currently the game is active in <#{channel[str(ctx.guild.id)]}>\n"
                                                 f"{count[str(ctx.guild.id)]} members have been eliminated so far.\n"
                                                 "Use `reset` to reset the count and stop the game.",inline=False)
            await ctx.send(embed=e)
        else:
            if channel[str(ctx.guild.id)] == 0:
                e=discord.Embed(color=discord.Colour.orange())
                e.add_field(name="Status: Inactive",value="The game isn't running currently.\n"
                                                          "Use `set_channel <channel_id>` to set the\n"
                                                          "battle ground channel and start playing the game.",inline=False)
                await ctx.send(embed=e)
            else:
                e = discord.Embed(color=discord.Colour.orange())
                e.add_field(name="Status: Inactive", value="The game isn't running currently.\n"
                                                       f"You can play the game in <#{channel[str(ctx.guild.id)]}>.",inline=False)
                await ctx.send(embed=e)

    @commands.command()
    @commands.guild_only()
    async def reset(self,ctx):
        orole=discord.utils.get(ctx.guild.roles, name="Operator")
        if orole in ctx.author.roles:
            with open("count.json","r") as f:
                count=json.load(f)
            count[str(ctx.guild.id)]=0
            with open("count.json","w") as f:
                json.dump(count,f)

            e=discord.Embed(color=discord.Colour.green())
            e.add_field(name="Reset Successfully",value="The kill count and the game has been reset.",inline=False)
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=discord.Colour.green())
            e.add_field(name="Missing Access",value="You need a role named `Operator` to use this command.",inline=False)
            await ctx.send(embed=e)


def setup(client):
    client.add_cog(Game(client))
