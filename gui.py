import PySimpleGUI as sg
from main import excecute

sg.theme('DarkBlue3')
layout = [  
    [sg.Multiline(size=(30, 10), key='textbox', font=('Helvetica', 20))],
    [sg.InputText('Course Name: ', size=(30, 4), key='course_name', font=('Helvetica', 20), pad=((10, 10), (10, 10)), tooltip='Course Name')],
    [sg.InputText('Group Name: ', size=(30, 4), key='group_name', font=('Helvetica', 20), pad=((10, 10), (10, 10)), tooltip='Group Name')],
    [sg.InputText('Group ID: ', size=(30, 4), key='group_id', font=('Helvetica', 20), pad=((10, 10), (10, 10)), tooltip='Group ID')],
    [sg.InputText('Date: ', size=(30, 4), key='date', font=('Helvetica', 20), pad=((10, 10), (10, 10)), tooltip='Date')],
    [sg.Button('Generate Certificates', font=('Helvetica', 20), pad=((10, 10), (10, 10)), tooltip='Generate Certificates')]
]

window = sg.Window('Window Title', layout, finalize=True)

window['course_name'].Widget.bind("<Button-1>", lambda event: window['course_name'].Widget.delete(0, 'end'))
window['group_name'].Widget.bind("<Button-1>", lambda event: window['group_name'].Widget.delete(0, 'end'))
window['group_id'].Widget.bind("<Button-1>", lambda event: window['group_id'].Widget.delete(0, 'end'))
window['date'].Widget.bind("<Button-1>", lambda event: window['date'].Widget.delete(0, 'end'))

while True:
    event, values = window.read()
    if event == 'Generate Certificates':
        firstnames = [values['textbox'].split()[x] for x in range(len(values['textbox'].split())) if x % 2 == 0]
        lastnames = [values['textbox'].split()[x] for x in range(len(values['textbox'].split())) if x % 2 != 0]
        full_names = [firstnames[x] + " " + lastnames[x] for x in range(len(firstnames))]
        print(excecute(full_names, values['course_name'], values['group_name'], values['group_id'], values['date']))
    elif event == sg.WIN_CLOSED:
        break
    else:
        print("Event not recognized.")

window.close()
