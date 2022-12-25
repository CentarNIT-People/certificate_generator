from docx import Document
from docxtpl import DocxTemplate

doc = DocxTemplate("./templates/nit_python.docx")
context = {
    "name" : "Nikola",
    "id" : "1.1",
    "course_name" : "Python",
    "group_name" : "Gimnazija",
    "group_id" : "1",
    "date": "2021-01-01",
}
doc.render(context)
# get a name of the picture currently in the document
media = doc.part.related_parts["rId4"], doc.part.related_parts["rId5"]
print(media[0].partname, media[1].partname)
doc.replace_media(media[0].partname, "./utilities/logo.png")

doc.save("test.docx")
