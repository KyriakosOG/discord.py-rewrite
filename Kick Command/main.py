import discord
from discord.ext import commands

client = commands.Bot(command_prefix="YOUR PREFIX")

@client.event
async def on_ready():
    print("Bot Is Online")

@client.command()
async def kick(ctx, member:discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} Has Been Kicked By {ctx.author.mention} For `{reason}` Successfully")
     
    #IF YOU WANT TO SEND HIM MESSAGE
    #await member.send("You Have Been Kicked")

client.run("TOKEN")