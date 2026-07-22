import os
from discord.ext import commands, tasks
import discord
from datetime import datetime
from zoneinfo import ZoneInfo

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

TZ = ZoneInfo("Asia/Ho_Chi_Minh")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    if not reminder.is_running():
        reminder.start()

@tasks.loop(minutes=1)
async def reminder():
    now = datetime.now(TZ)

    # Thứ 2 - Thứ 6
    if now.weekday() < 5:
        if now.hour == 15 and now.minute == 10:
            channel = bot.get_channel(CHANNEL_ID)
            if channel:
                await channel.send(
                    "@everyone\n\n⏰ **Reminder Alert!**\n\nNhớ điền KPI nha mn 📋"
                )

bot.run(TOKEN)
