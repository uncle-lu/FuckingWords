#coding:utf-8

import pdfkit
import os

options = {
    'page-size': 'A4',
    'margin-top':'0.2in',
    'margin-right':'0.2in',
    'margin-bottom':'0.2in',
    'margin-left':'0.2in',
    'encoding':"UTF-8",
}

f = open('in.html').read()

pdfkit.from_string(f,'out.pdf',options=options)
