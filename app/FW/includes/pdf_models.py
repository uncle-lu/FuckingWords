#coding:utf-8

import pdfkit
import os
import random
from FW.models import Words, Units, Pdfs
from jinja2 import Environment

def create_list(W_count,U_list):
    L = []
    U_count = len(U_list)

    while W_count > 0:

        for this_Unit in U_list:
            U = Units.objects(Title=this_Unit).first()
            li = U.List

            if W_count / U_count > len(li):
                li = random.shuffle(li)
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

def create_str(L,U_list):
    s = U_list
    left = ''
    right = ''
    c = 1 
    if len(L) > 50 :
        while c <=50 :
            left = left + '\n<p>%d %s</p>' % (c,L[c-1])
            c = c + 1
        while c <= len(L):
            right = right + '\n<p>%d %s</p>' % (c,L[c-1])
            c = c + 1
    else :
        while c <= len(L):
            left = left + '\n<p>%d %s</p>' % (c,L[c-1])
            c = c + 1
    
    return (s,left,right)


def create_pdf(W_count, U_list):
    L = create_list(W_count,U_list)

    s,left,right = create_str(L,U_list)

    f = open('static/m1.html').read()

    html = Environment().from_string(f).render(title=s, left=left,right=right)

    options = {
        'page-size': 'A4',
        'margin-top': '0.2in',
        'margin-right': '0.2in',
        'margin-bottom': '0.2in',
        'margin-left': '0.2in',
        'encoding': "UTF-8",
        'quiet':''
    }

    Id =  len(Pdfs.objects) +1
    pdf = pdfkit.from_string(html,False,options=options)

    Pdfs(Id = Id,Title='%d_%s' % (W_count,U_list), File=pdf).save()

    return Id