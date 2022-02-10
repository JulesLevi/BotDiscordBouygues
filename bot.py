import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.reply('Hello!', mention_author=True)

client = MyClient()
client.run('OTQxMzY2MTc5NTM1MTQyOTgy.YgU5kg.SLqmirFN8vhNzUuqb1uE2IIf-gI')