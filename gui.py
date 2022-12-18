import PySimpleGUI as sg
from main import excecute


sg.theme('DarkBlue3')
layout = [  
            [sg.Multiline(size=(30, 10), key='textbox', font=('Helvetica', 20))],
            [sg.InputText('', size=(30, 4), key='course_name', font=('Helvetica', 20), pad=((10, 10), (10, 10)), tooltip='Course Name')],
            [sg.InputText('', size=(30, 4), key='group_name', font=('Helvetica', 20), pad=((10, 10), (10, 10)), tooltip='Group Name')],
            [sg.InputText('', size=(30, 4), key='group_id', font=('Helvetica', 20), pad=((10, 10), (10, 10)), tooltip='Group ID')],
            [sg.Button('Generate Certificates', font=('Helvetica', 20), pad=((10, 10), (10, 10)), tooltip='Generate Certificates')]
        ]

window = sg.Window('Window Title', layout)
while True:
    event, values = window.read()
    if event == 'Generate Certificates':
        firstnames = [values['textbox'].split()[x] for x in range(len(values['textbox'].split())) if x % 2 == 0]
        lastnames = [values['textbox'].split()[x] for x in range(len(values['textbox'].split())) if x % 2 != 0]
        full_names = [firstnames[x] + " " + lastnames[x] for x in range(len(firstnames))]
        print(excecute(full_names, values['course_name'], values['group_name'], values['group_id']))
    elif event == sg.WIN_CLOSED:
        break
    else:
        pass


window.close()

