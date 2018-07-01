#coding:utf-8

import pdfkit
import os

options = {
    'page-size': 'Letter',
    'margin-top':'0.1in',
    'margin-right':'0.1in',
    'margin-bottom':'0.1in',
    'margin-left':'0.1in',
    'encoding':"UTF-8",
}

f = open('in.html').read()

pdfkit.from_string(f,'out.pdf',options=options)
