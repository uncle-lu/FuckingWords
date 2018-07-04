#coding:utf-8

from flask import render_template, redirect, url_for, flash, abort, send_file, request
from FW.views import Create_pdf_views
from FW.models import Units, Words, Pdfs
from FW.includes.pdf_models import create_pdf
from FW.forms import Create_pdfForm

@Create_pdf_views.route('/',methods=['GET','POST'])
def index():
    Up = str(request.args.get('Title',''))
    F = Create_pdfForm()

    if F.validate_on_submit():
        U_list = F.Units_list.data.split(',')
        Id = create_pdf(int(F.Words_count.data),U_list)
        return redirect(url_for('Create_pdf_views.pdf_down',Id = Id))
    
    F.Units_list.data = Up
    
    return render_template('C/index.html',title =u'生成' ,F = F)

@Create_pdf_views.route('/list',methods=['GET','POST'])
def pdf_list():
    P = Pdfs.objects().all()

    l = []

    for p in P:
        l.append({
            'Id':int(p.Id),
            'Title':p.Title
        })
    
    return render_template('C/list.html',title='Pdf list',p = l)

@Create_pdf_views.route('/Id/<int:Id>',methods=['GET','POST'])
def pdf_down(Id):
    P = Pdfs.objects(Id = Id).first()

    if P == None:
        abort(404)

    p = P.File

    return send_file(p,attachment_filename='%d.pdf' % Id)

@Create_pdf_views.route('/delete')
def delete():
    P = Pdfs.objects().all()

    for p in P:
        p.delete()
    
    flash('Yeah!')

    return redirect(url_for('Create_pdf_views.pdf_list'))