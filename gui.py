import PySimpleGUI as sg
from main import excecute

sg.theme('DarkBlue3')
layout = [  
    [sg.Multiline(size=(30, 10), key='textbox', font=('Helvetica', 20))],
    [sg.InputText('', size=(30, 4), key='course_name', font=('Helvetica', 20), pad=((10, 10), (10, 10)), tooltip='Course Name')],
    [sg.InputText('', size=(30, 4), key='group_name', font=('Helvetica', 20), pad=((10, 10), (10, 10)), tooltip='Group Name')],
    [sg.InputText('', size=(30, 4), key='group_number', font=('Helvetica', 20), pad=((10, 10), (10, 10)), tooltip='Group Number')],
    [sg.InputText('', size=(30, 4), key='group_id', font=('Helvetica', 20), pad=((10, 10), (10, 10)), tooltip='Group ID')],
    [sg.InputText('', size=(30, 4), key='date', font=('Helvetica', 20), pad=((10, 10), (10, 10)), tooltip='Date')],
    [sg.Button('Generate Certificates', font=('Helvetica', 20), pad=((10, 10), (10, 10)), tooltip='Generate Certificates')]
]

window = sg.Window('Window Title', layout, finalize=True)

while True:
    event, values = window.read()
    if event == 'Generate Certificates':
        firstnames = [values['textbox'].split()[x] for x in range(len(values['textbox'].split())) if x % 2 == 0]
        lastnames = [values['textbox'].split()[x] for x in range(len(values['textbox'].split())) if x % 2 != 0]
        full_names = [firstnames[x] + " " + lastnames[x] for x in range(len(firstnames))]
        values = {
            "full_names": full_names,
            "course_name": values['course_name'],
            "group_name": values['group_name'],
            "group_number": values['group_number'],
            "group_id": values['group_id'],
            "date": values['date']
        }
        print(excecute(values))
    elif event == sg.WIN_CLOSED:
        break
    else:
        print("Event not recognized.")
window.close()
