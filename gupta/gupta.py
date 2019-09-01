import discord
from redbot.core import commands, Config, checks
from redbot.core.utils.embed import randomize_colour
from redbot.core.utils.menus import menu, DEFAULT_CONTROLS
from random import choice


class Gupta(commands.Cog):


    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['ripgupta'])
    async def ripgupta(self, ctx, count, *, message):
        """Put in a sizeable number and put a message afterward"""
        int(count)
        gupta = 468209010978455552
        channel = 617525238392946699
        mloop = 0
        
        while mloop > count:
            await channel.send("{} {}".format(gupta.mention, message))
            int(mloop)
            mloop = mloop + 1
    
