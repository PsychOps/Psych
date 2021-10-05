import discord
from settings import config, botcogs
import traceback
from discord.ext import commands


def get_prefix(bot, message):
    prefixes = [";"]

    return commands.when_mentioned_or(*prefixes)(bot, message)


#  bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True,
#  allowed_mentions=discord.AllowedMentions(roles=False, users=False, everyone=False))

bot = commands.Bot(
    command_prefix=get_prefix,
    case_insensitive=True,
    allowed_mentions=discord.AllowedMentions.none(),
    max_messages=10000,
    intents=discord.Intents.all(),
    status=discord.Status.online,
    activity=discord.Activity(type=discord.ActivityType.playing, name=f'in the sandbox'),
    description="your mom.",
    slash_commands=True,
    slash_command_guilds=[820256957369679882]
)


@commands.Cog.listener()
async def on_ready():
    print('Bot has started successfully.')


for extension in botcogs.extensions:
    try:
        bot.load_extension(extension)
        print(f'[extension] {extension} was loaded successfully!')
    except Exception as e:
        tb = traceback.format_exception(type(e), e, e.__traceback__)
        tbe = "".join(tb) + ""
        print(f'[WARNING] Could not load extension {extension}: {tbe}')

bot.run(config.token)