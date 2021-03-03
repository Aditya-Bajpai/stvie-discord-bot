import discord
from discord.ext import commands
import random
import praw
from keep_alive import keep_alive





bot = commands.Bot(command_prefix="$")
reddit = praw.Reddit(client_id="9hJoAca6aUNJDw",
                     client_secret="NCl7KTMEqaWue0oB61m6LlUM5zHKxA",
                     username="Adi_who_doesnt_simp",
                     password="Adi@1234",
                     user_agent="prawpraw",
                     check_for_async=False)
subreddit = reddit.subreddit('MinecraftMemes')
top = subreddit.top(limit=5)



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('memes'))
    print("Stevie is online")


@bot.command()
async def ping(ctx):
    await ctx.send(f'The ping is {round(bot.latency*1000)}ms')


@bot.command(aliases=['8ball', 'eight', 'test' , "Eight"])
async def _8ball(ctx, *, question):
    responses = [
        'Yes , definitely', 'No', 'It is doubtful', 'It is certain',
        'Not in a million years', 'There is a possibility', 'Ofcourse',
        'Ofcourse not', 'Yes You legend', 'NO YOU DUMBO'
    ]
    if question.endswith('?'):
        await ctx.send(
            f'Question: {question}\nAnswer: {random.choice(responses)}')
    else:
        await ctx.send(
            "Your question has to be a question you measly being (end it with a question mark)"
        )


@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, *, amount=0):
  if amount == 0:
    await ctx.send("Specify the number of messages to clear dumbo")
  else :
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Cleared {amount} messages")


@bot.command()
async def meme(ctx , subred = 'MinecraftMemes'):
    subreddit = reddit.subreddit(subred)
    all_subs = []
    top = subreddit.top(limit=500)
    for meme in top:
        all_subs.append(meme)
    random_meme = random.choice(all_subs)
    name = random_meme.title
    url = random_meme.url
    em = discord.Embed(title=name, colour=discord.Colour.green())
    em.set_image(url=url)
    await ctx.send(embed=em)


@bot.command()
async def intro(ctx):
    emba = discord.Embed(title="Hello Plebians",
                         descripton="My Name is Steve",
                         colour=discord.Color.blue())
    emba.add_field(name="Who am I ?",
                   value='I am the king bitches.',
                   inline=False)
    await ctx.send(embed=emba)


@bot.command(aliases=['fs'])
async def f(ctx ,*, to):
    emb = discord.Embed(title="F",
                        description="respects",
                        colour=discord.Color.red())
    emb.add_field(name=f"{ctx.author.display_name} has paid their respects for {to}",
                  value="👊")
    await ctx.send(embed=emb)

@bot.command()
async def flat_earth(ctx):
  await ctx.send(f"NO IT'S NOT. @here {ctx.author.display_name} is dumb.")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx , member:discord.Member,*,reason="Reason Not Provided"):
  try:
    await member.kick()
    await member.send(f"You have been kicked by {ctx.author.display_name}\nReason: {reason}")
    await ctx.send(f"{ctx.author.display_name} kicked {member}\nReason:  {reason}")
  except discord.Forbidden:   
    await ctx.send(f"I don't have permission to kick **{member}**")


@bot.command()
async def steve_thicc(ctx):
  await ctx.send(file=discord.File('tsm.jpg')) 

@bot.command()
async def poll(ctx ,* , msg):
  emb = discord.Embed(title = f"Poll initiated by {ctx.author.display_name}" , description = f"{msg}")
  msg = await ctx.send(embed = emb)
  await msg.add_reaction("👍")
  await msg.add_reaction("👎")


with open("nono.0", "r", encoding="utf-8") as f:
    token = f.read()

keep_alive()

bot.run(token)
