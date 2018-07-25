# coding : utf-8

from docx import Document
from docx.shared import Cm, Pt
import io

document = Document()

p = document.add_paragraph(u'New things.呵呵呵enenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenen呵enenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenenen')

k = p.style.paragraph_format
k.line_spacing = Cm(0.5)

sections = document.sections
for section in sections:
    section.top_margin = Cm(1)
    section.bottom_margin = Cm(1)
    section.left_margin = Cm(1)
    section.right_margin = Cm(1)

new = 
document.save(new)

print(new)