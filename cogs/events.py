from discord.ext import commands
import json


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ready! Logged in as {0.user}".format(self.client))

    async def on_message(self, message):
        if message.author == self.client.user:
            return

    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        with open("channels.json","r") as f:
            channel = json.load(f)
        channel[str(guild.id)]=0
        with open("channels.json", "w") as f:
            json.dump(channel,f)

        with open("count.json","r") as f:
            count=json.load(f)
        count[str(guild.id)]=0
        with open("count.json","w") as f:
            json.dump(count,f)


def setup(client):
    client.add_cog(Events(client))
