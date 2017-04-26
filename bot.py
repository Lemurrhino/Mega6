import discord
from discord.ext import commands
import logging
import ConfigParser

configParser = ConfigParser.RawConfigParser()
configFilePath = r'c:\abc.txt'
configParser.read(configFilePath)

token = ''
bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'), description='SELLLLLFFFF BOT!', self_bot=True)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# extensions to be loaded on startup
startup_extensions = ['moderator']

async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))
    print('Bot is ready to respond to commands')
    await bot.change_presence(game="Type '$help' for help | LimeBots: https://discord.gg/WvwCHdz")

# loads extensions (in cogs format)
    if __name__ == "__main__":
        for extension in startup_extensions:
            try:
                bot.load_extension(extension)
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__, e)
                print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(token)
