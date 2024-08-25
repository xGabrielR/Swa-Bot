import FreeSimpleGUI as sg

layout = [
    [sg.Text("What's your name?")],
    [sg.InputText()],
    [sg.Button("Ok"), sg.Button("Cancel")]
]

window = sg.Window("Hello Example", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Cancel":
        break

    print("Hello", values[0], "!")

window.close()