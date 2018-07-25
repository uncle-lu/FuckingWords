# coding:utf-8

from FW.models import Words, Units, Pdfs
import random
import io
from docx import Document
from docx.shared import Cm, Pt

def create_list(W_count,U_list):
    L = []
    U_count = len(U_list)

    while W_count > 0:

        for this_Unit in U_list:
            U = Units.objects(Title=this_Unit).first()
            li = U.List

            if W_count / U_count > len(li):
                random.shuffle(li)
                for this_word in li:
                    L.append(Words.objects(Title=this_word).first().Meaning)
                W_count = W_count - len(li)
                U_count = U_count - 1
            else:
                k = W_count / U_count

                while k > 0:
                    wo = random.choice(li)
                    Mean = Words.objects(Title=wo).first().Meaning

                    if Mean in L:
                        continue
                    else:
                        k = k - 1
                        W_count = W_count - 1
                        L.append(Mean)
    
    return L

def create_str(L):

    page = ''

    c = 1

    while c <= len(L):
        page = page + u'%d.%s\n' % (c,L[c-1])
        c = c + 1

    return page

def create_docx(W_count, U_list):
    L = create_list(W_count,U_list)
    
    page = create_str(L)

    document = Document() 
    p = document.add_paragraph(page)
    k = p.style.paragraph_format
    k.line_spacing = Cm(0.5)

    sections = document.sections
    for section in sections:
        section.top_margin = Cm(1)
        section.bottom_margin = Cm(1)
        section.left_margin = Cm(1)
        section.right_margin = Cm(1)

    Id =  len(Pdfs.objects) +1

    doc = Pdfs(Id = Id,Title='%d_%s' % (W_count,U_list))

    document.save(doc.File)

    doc.save()

    return Id