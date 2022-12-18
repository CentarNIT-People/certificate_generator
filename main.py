import os
from docx2pdf import convert
from docxtpl import DocxTemplate

def excecute(list_of_names, course_name, group_name, group_id):
    for index, name in enumerate(list_of_names):
        file_name = str(name).replace(" ", "_")
        doc = DocxTemplate("template.docx")
        context = { 
            "name" : name,
            "id" :f"1.{index+1}",
            "course_name" : course_name,
            "group_name" : group_name,
            "group_id" : group_id,
            "date": "23.12.2022"
            # TODO: date of issue
            # TODO: image
            # TODO: color
        }
        doc.render(context)
        os.chdir("results")
        doc.save(f"{file_name}.docx")
        convert(f"{file_name}.docx")
        os.chdir("..")
    quit()

