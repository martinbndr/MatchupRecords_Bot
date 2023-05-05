import sqlite3
import os, json

import discord
from discord.ext import commands

with open(os.path.join('config.json'), 'r') as f:
    CONFIG = json.load(f)

db = sqlite3.connect('scores.sqlite')
cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS scores(guild_id BIGINT, user_id BIGINT, opponent_id BIGINT, wins BIGINT DEFAULT 0, losses BIGINT DEFAULT 0);
''')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or(CONFIG['PREFIX']), intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is now ready!')

@bot.command(name='updatematchuprecords', description='Will store/update records accordingly, and will add new users to the record.')
async def updatematchuprecords(ctx: commands.Context, user1: discord.Member, win1: int, user2: discord.Member, win2: int):
    cursor.execute('SELECT * FROM scores WHERE guild_id = ? AND user_id = ? AND opponent_id = ?', (ctx.guild.id, user1.id, user2.id))
    userdata = cursor.fetchone()
    if not userdata:
        cursor.execute('INSERT INTO scores VALUES (?,?)')

if __name__ == '__main__':
    bot.run(CONFIG['TOKEN'])