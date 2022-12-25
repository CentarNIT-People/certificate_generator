from docx import Document
from docx.shared import Inches
from docxtpl import DocxTemplate, InlineImage

doc = DocxTemplate("./templates/nit_python.docx")
image = InlineImage(doc, 'utilities/logo.png', width=Inches(30), height=Inches(10))
context = {
    "name" : "Nikola",
    "id" : "1.1",
    "course_name" : "Python",
    "group_name" : "Gimnazija",
    "group_id" : "1",
    "date": "2021-01-01",
    "image": image
}
doc.render(context)
doc.save("test.docx")
