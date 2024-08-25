import time
import discord
import FreeSimpleGUI as sg
from discord.ext.commands import Bot

from datetime import datetime

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

sg.theme("Black")

bot = Bot(command_prefix="!", intents=intents)

TOKEN = ""

LAYOUT = [
    [sg.Text("▃▃▃▃▃▃ ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃\n\n▃   Discord Bot\n\n▃   Bot Para Mensagens da LIB!\n\n▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃ ▃▃▃▃▃▃")], 
    [sg.Text(" ")],
    [sg.Button("Info")],
    [sg.Multiline(key="msg_input_user", size=(40,10), pad=(10,10))],
    [sg.Button("Enviar Mensagem no PV")],
    [sg.Text(" ")]
]

WINDOW = sg.Window(
    "Discord Bot",
    layout=LAYOUT,
    element_justification="c"
)

@bot.event
async def on_ready():
    print(f"Logged!")
    while True:
        event, values = WINDOW.read()

        if event == sg.WIN_CLOSED or event == "Cancel":
            exit()

        if event == "Info":
            sg.popup("Olá Mundo")

        if event == "Enviar Mensagem no PV":
            msg = values["msg_input_user"]

            if not msg:
                sg.popup("Escreve a mensagem man")
            
            else:
                sg.popup("Iniciando o envio das mensagens, pfvr, aguarde...")
                guild: discord.Guild = bot.get_guild(1277271796055412770)

                for member in guild.members:
                    if member.id == 936297874831052880:
                        user = await bot.fetch_user(member.id)
                        await user.send(msg)
                
                time.sleep(10)

                sg.popup("Envio finalizado!")

if __name__ == "__main__":
    bot.run(TOKEN)
