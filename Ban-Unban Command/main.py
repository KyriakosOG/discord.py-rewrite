import discord
from discord.ext import commands

client = commands.Bot(command_prefix="YOUR PREFIX")

@client.event
async def on_ready():
    print("Bot Is Online")

@client.command()
async def ban(ctx, member:discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} Has Been Banned By {ctx.author.mention} For `{reason}` Successfully")

    #IF YOU WANT TO SEND HIM MESSAGE
    #await member.send("You Have Been Banned")

@client.command()
async def unban(ctx, *, member):
    banned_users= await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{member} Has Been Banned By {ctx.author.mention} Successfully")

client.run("TOKEN")