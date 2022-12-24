import os
import convertapi
from docxtpl import DocxTemplate

# def convert_to_pdf():
#     os.chdir("results")
#     for file in os.listdir():
#         if file.endswith(".docx"):
#             convertapi.api_secret = '59fywzlChxa3iNc7'
#             convertapi.convert('pdf', {
#                 'File': file
#             }, from_format = 'docx').save_files('../pdf')
#     os.chdir("..")

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
            # TODO: date of issue
            # TODO: image
            # TODO: style of certificate
        }
        doc.render(context)
        os.chdir("results")
        doc.save(f"{file_name}.docx")
        os.chdir("..")
    # convert_to_pdf()
    return "Done"

