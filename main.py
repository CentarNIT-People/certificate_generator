import os
from pathlib import Path
from docxtpl import DocxTemplate
from pdf2image import convert_from_path
from utilities.mail.send import send_mail, get_all_pdf_files
from utilities.mail.constants import SENDER_EMAIL, SENDER_PASSWORD, RECIPIENTS

def get_user_input():
    print("1. GUI")
    print("2. Converter")
    mode = input("Please select the mode you want to use: ")
    if mode == "1":
        try:
            os.system("python3 gui.py")
        except:
            os.system("python gui.py")
    elif mode == "2":
        print("1. Docx to PDF")
        print("2. PDF to Images")
        converter_mode = input("Please select the mode you want to use: ")
        if converter_mode == "1":
            convert_to_pdf()
            print("Done")
        elif converter_mode == "2":
            convert_to_image()
            print("Done")
    else:
        print("Invalid mode")
        get_user_input()

def parse(values: dict):
    for index, name in enumerate(values["full_names"]):
        file_name = str(name).replace(" ", "_")
        doc = DocxTemplate(values["template"])
        context = {
            "name" : name.strip(),
            "id" :f"{values['group_number']}.{index+1}".strip(),
            "course_name" : values["course_name"].strip(),
            "group_name" : values["group_name"].strip(),
            "group_id" : values["group_id"].strip(),
            "date": values["date"].strip(),
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
    for file in os.listdir("results/docx"):
        if file.endswith(".docx"):
            os.system(f"/Applications/LibreOffice.app/Contents/MacOS/soffice --headless --convert-to pdf results/docx/{file} --outdir results/pdf")

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

if __name__ == "__main__":
    get_user_input()