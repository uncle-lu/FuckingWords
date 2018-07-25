from docx import Document

document = Document()

from docx.enum.style import WD_STYLE_TYPE
styles = document.styles

paragraph_styles = [
     s for s in styles 
 ]

for style in paragraph_styles:
    print(style.name)
