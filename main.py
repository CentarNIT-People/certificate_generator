# TODO: add feature to insert image
# TODO: add more templates
# TODO: add more option
# TODO: style of certificate
# TODO: make it so that it doesn't break after the process is done

import os
from pathlib import Path
from docx2pdf import convert
from docxtpl import DocxTemplate
from pdf2image import convert_from_path

def convert_to_image():
    pdf_dir = Path("pdf")
    for file in pdf_dir.glob("*.pdf"):
        images = convert_from_path(file)
        for index, image in enumerate(images):
            image.save(f"images/{file.stem}_{index}.png", "PNG")

def convert_to_pdf():
    os.chdir("results")
    filenames = os.listdir()
    os.chdir("..")
    for filename in filenames:
        if filename.endswith(".docx"):
            convert(filename, f"pdf/{filename}.pdf")
    

def excecute(list_of_names, course_name, group_name, group_id, date):
    # template = input("Enter template name: ")
    for index, name in enumerate(list_of_names):
        file_name = str(name).replace(" ", "_")
        doc = DocxTemplate("./templates/gimnazija_python.docx")
        context = { 
            "name" : name,
            "id" :f"1.{index+1}",
            "course_name" : course_name,
            "group_name" : group_name,
            "group_id" : group_id,
            "date": date
        }
        doc.render(context)
        os.chdir("results")
        doc.save(f"{file_name}.docx")
        os.chdir("..")
    convert_to_pdf()
    convert_to_image()
    return "Done"
