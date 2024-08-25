import discord
from discord.ext.commands import Bot

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = Bot(command_prefix="!", intents=intents)

TOKEN = ""

@bot.command("envia")
async def envia_mensagem_privado(ctx, message: str = None):
    if not message:
        await ctx.channel.send("Informe a mensagem :(")

    else:
        guild: discord.Guild = bot.get_guild(1277271796055412770)

        for member in guild.members:
            if member.id == 936297874831052880:
                user = await bot.fetch_user(member.id)
                await user.send(message)

@bot.event
async def on_ready():
    print(f"Logged!")

if __name__ == "__main__":
    bot.run(TOKEN)
