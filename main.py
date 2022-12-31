import os
from pathlib import Path
from docx2pdf import convert
from docxtpl import DocxTemplate
from pdf2image import convert_from_path
from utilities.mail.send import send_mail, get_all_pdf_files
from utilities.mail.constants import SENDER_EMAIL, SENDER_PASSWORD, RECIPIENTS

def parse(values: dict):
    for index, name in enumerate(values["full_names"]):
        file_name = str(name).replace(" ", "_")
        doc = DocxTemplate(values["template"])
        context = {
            "name" : name,
            "id" :f"{values['group_number']}.{index+1}",
            "course_name" : values["course_name"],
            "group_name" : values["group_name"],
            "group_id" : values["group_id"],
            "date": values["date"]
        }
        doc.render(context)
        if values["logo"] != "":
            doc.replace_pic("logo.png", values["logo"])
        doc.save(f"results/docx/{file_name}.docx")

def convert_to_image():
    pdf_dir = Path("results/pdf")
    for file in pdf_dir.glob("*.pdf"):
        images = convert_from_path(file)
        for _, image in enumerate(images):
            image.save(f"results/images/{file.stem}.png", "PNG")

def convert_to_pdf():
    os.chdir("results/docx")
    filenames = os.listdir()
    os.chdir("..")
    for filename in filenames:
        if filename.endswith(".docx"):
            convert(f"docx/{filename}", f"pdf/{filename}.pdf")
    

def excecute(values: dict):
    parse(values)
    convert_to_pdf()
    convert_to_image()
    send_mail(
        SENDER_EMAIL,
        SENDER_PASSWORD,
        RECIPIENTS,
        get_all_pdf_files()
    )
    return "Done"
