import discord
from discord.ext import commands

client = commands.Bot(command_prefix="YOUR PREFIX")

@client.event
async def on_ready():
    print("Bot Is Online")

@client.command()
async def mute(ctx, member:discord.Member, *, reason=None):
    guild = ctx.guild
    muteRole = discord.utils.get(guild.roles, name="Muted")

    if not muteRole:
        muteRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(muteRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)
    await member.add_roles(muteRole, reason=reason)
    await ctx.send(f"{member.mention} Has Been Muted By {ctx.author.mention} For `{reason}` Successfully")

    #IF YOU WANT TO SEND HIM MESSAGE
    #await member.send("You Have Been Muted")

@client.command()
async def unmute(ctx, member:discord.Member):
    guild = ctx.guild
    muteRole = discord.utils.get(guild.roles, name="🔇Muted")

    await member.remove_roles(muteRole)
    await ctx.send(f"{member.mention} Has Been Muted By {ctx.author.mention} Successfully")
     
    #IF YOU WANT TO SEND HIM MESSAGE
    #await member.send("You Have Been Unmuted")

client.run("TOKEN")