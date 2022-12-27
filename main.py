# DONE: add feature to insert image   
# TODO: style of certificate
# DONE: make it so that it doesn't break after the process is done

import os
from pathlib import Path
from docx2pdf import convert
from docxtpl import DocxTemplate
from pdf2image import convert_from_path

def parse(values: dict):
    for index, name in enumerate(values["full_names"]):
        file_name = str(name).replace(" ", "_")
        doc = DocxTemplate("./templates/nit_python.docx")
        context = { 
            "name" : name,
            "id" :f"1.{index+1}",
            "course_name" : values["course_name"],
            "group_name" : values["group_name"],
            "group_id" : values["group_id"],
            "date": values["date"]
        }
        doc.render(context)
        doc.replace_pic("logo.png", "utilities/logo.png")
        doc.save(f"results/{file_name}.docx")

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
    

def excecute(values: dict):
    parse(values)
    convert_to_pdf()
    convert_to_image()
    return "Done"

if __name__ == "__main__":
    try:
        os.system("python3 gui.py")
    except:
        os.system("python gui.py")
