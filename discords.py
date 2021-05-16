import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="o!",intents=discord.Intents.all(),self_bot = True)


token = ""
#YOUR TOKEN



@bot.command()
async def embed(ctx,title,description,footer,thumbnail,footericon):
    embed = discord.Embed(title=str(title), description=str(description), color=discord.Color.blue())
    embed.set_thumbnail(url=str(thumbnail))
    embed.set_footer(text=str(footer),icon_url=str(footericon))
    await ctx.send(embed=embed)


bot.run(token,bot=False,reconnect=True) 
