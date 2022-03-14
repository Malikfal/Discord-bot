import discord
from os import  getenv

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='За погодой!'))

    async def on_message(self, message):
        if message.author == self.user:
            return
        elif message.content.startswith('привет'):
            await message.channel.send(f'И тебе привет {message.author.mention}')

client = MyClient()
client.run(getenv('TOKEN'))