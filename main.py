# TODO: add feature to insert image
# TODO: add more templates
# TODO: add more option
# TODO: style of certificate
# TODO: make it so that it doesn't break after the process is done

import os
from pathlib import Path
from docx import Document
from docx2pdf import convert
from docx.shared import Inches
from docxtpl import DocxTemplate
from pdf2image import convert_from_path

def parse(*args):
    for index, name in enumerate(args[0]):
        file_name = str(name).replace(" ", "_")
        doc = DocxTemplate("./templates/nit_python.docx")
        context = { 
            "name" : name,
            "id" :f"1.{index+1}",
            "course_name" : args[1],
            "group_name" : args[2],
            "group_id" : args[3],
            "date": args[4]
        }
        doc.render(context)
        os.chdir("results")
        doc.save(f"{file_name}.docx")
        doc_new = Document(f"{file_name}.docx")
        doc_new.add_picture("./utilities/logo.png")
        doc_new.save(f"{file_name}.docx")
        os.chdir("..")

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
    

def excecute(*args):
    # template = input("Enter template name: ")
    parse(*args)
    convert_to_pdf()
    convert_to_image()
    return "Done"