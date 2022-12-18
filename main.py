import os
import convertapi
from os import walk
from docxtpl import DocxTemplate
from pdf2image import convert_from_path

def convert_to_pdf():
    os.chdir("results")
    for file in os.listdir():
        if file.endswith(".docx"):
            convertapi.api_secret = '59fywzlChxa3iNc7'
            convertapi.convert('pdf', {
                'File': file
            }, from_format = 'docx').save_files('../pdf')
    os.chdir("..")

def convert_to_image():
    f = []
    for (_, _, filenames) in walk("./pdf"):
        f.extend(filenames)
        break

    for x in f:
        if x.endswith(".pdf"):
            pages = convert_from_path(f'./files/{x}')

            for i in range(len(pages)):
                pages[i].save(f'./results/{str(x)}' +'.jpg', 'JPEG')

def excecute(list_of_names, course_name, group_name, group_id, date):
    for index, name in enumerate(list_of_names):
        file_name = str(name).replace(" ", "_")
        doc = DocxTemplate("template.docx")
        context = { 
            "name" : name,
            "id" :f"1.{index+1}",
            "course_name" : course_name,
            "group_name" : group_name,
            "group_id" : group_id,
            "date": date
            # TODO: date of issue
            # TODO: image
            # TODO: style of certificate
        }
        doc.render(context)
        os.chdir("results")
        doc.save(f"{file_name}.docx")
        os.chdir("..")
    convert_to_pdf()
    convert_to_image()
    return "Done"


convert_to_pdf()
convert_to_image()