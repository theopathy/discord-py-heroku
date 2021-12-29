import os
import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")
    activity = discord.Game(name="Gaslighting", type=3)
    await bot.change_presence(status=discord.Status.watching, activity=activity)

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

if __name__ == "__main__":
    bot.run(TOKEN)

# When user says Hello Reply back
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.content.startswith("a"):
        await message.channel.send("dont be a dick")
