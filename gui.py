from main import excecute
import PySimpleGUI as sg, os
from utilities.gui_utils.gui_placeholder import setPlaceholder

sg.theme('DarkBlue3')

placeholders = ["Course Name", "Group Name", "Group Number", "Group ID", "Date", "Certificate Logo", "Certificate Template"]

layout = [  
    [sg.Multiline(size=(100, 12), key='textbox', font=('Helvetica', 20))],
    [sg.InputText('', size=(100, 4), key='Course Name', font=('Helvetica', 20), pad=((10, 10), (10, 10)), tooltip=placeholders[0])],
    [sg.InputText('', size=(100, 4), key='Group Name', font=('Helvetica', 20), pad=((10, 10), (10, 10)), tooltip=placeholders[1])],
    [sg.InputText('', size=(100, 4), key='Group Number', font=('Helvetica', 20), pad=((10, 10), (10, 10)), tooltip=placeholders[2])],
    [sg.InputText('', size=(100, 4), key='Group ID', font=('Helvetica', 20), pad=((10, 10), (10, 10)), tooltip=placeholders[3])],
    [sg.InputText('', size=(100, 4), key='Date', font=('Helvetica', 20), pad=((10, 10), (10, 10)), tooltip=placeholders[4])],
    [
        sg.FileBrowse('Browse Logo', initial_folder=os.getcwd()+"/utilities/images/", key='Certificate Logo', font=('Helvetica', 20), pad=((10, 10), (10, 10)), tooltip=placeholders[5]),
        sg.FileBrowse('Browse Template', initial_folder=os.getcwd()+"/utilities/templates/", key='Certificate Template', font=('Helvetica', 20), pad=((10, 10), (10, 10)), tooltip=placeholders[6]),
        sg.Button('Generate Certificates', font=('Helvetica', 20), pad=((10, 10), (10, 10)), tooltip='Generate Certificates')
    ]
]


window = sg.Window('Window Title', layout, finalize=True, size=(800, 850))
for placeholder in placeholders:
    setPlaceholder(window[placeholder], placeholder + ":")

while True:
    event, values = window.read()
    if event == 'Generate Certificates':
        firstnames = [values['textbox'].split()[x] for x in range(len(values['textbox'].split())) if x % 2 == 0]
        lastnames = [values['textbox'].split()[x] for x in range(len(values['textbox'].split())) if x % 2 != 0]
        full_names = [firstnames[x] + " " + lastnames[x] for x in range(len(firstnames))]
        values = {
            "full_names": full_names,
            "course_name": values['Course Name'],
            "group_name": values['Group Name'],
            "group_number": values['Group Number'],
            "group_id": values['Group ID'],
            "logo": values['Certificate Logo'],
            "template": values['Certificate Template'],
            "date": values['Date'],
        }
        if values['logo'] != '':
            values['logo'] = values['logo']
        else:
            values['logo'] = 'logo.png'
        print(excecute(values))
    elif event == sg.WIN_CLOSED:
        break
    else:
        print("Event not recognized.")
window.close()
