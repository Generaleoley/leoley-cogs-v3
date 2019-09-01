import discord
from redbot.core import commands, Config, checks
from redbot.core.utils.embed import randomize_colour
from redbot.core.utils.menus import menu, DEFAULT_CONTROLS
from random import choice


class Gupta(commands.Cog):


    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['ripgupta'])
    async def ripgupta(self, ctx, count=int):
    
