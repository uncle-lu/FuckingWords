# coding : utf-8

from flask import render_template, redirect, url_for, flash, request, abort
from FW.models import Words
from FW.forms import WordsForm
from . import Words_views

@Words_views.route('/', methods=['GET', 'POST'])
def index():
    page = 1
    try request.args.get('page',''):
        page = request.args.get('page','')
    
    Lis = Words.objects.paginate(page= page,per_page=25)

    return render_template('W/index.html',title= 'Words',L = Lis)

@Words_views.route('/<string:T>', methods=['GET', 'POST'])
def ones(T):
    
    Wo = Words.objects(Title=T).first()

    return render_template('W/ones.html', title=Wo.Title, Wo = Wo)

@Words_views.route('/change',methods=['GET','POST'])
def change():

    change_title = request.args.get('title','')

    Wo = Words.objects(Title=change_title).first()

    if Wo is None:
        abort(404)

    Form = WordsForm()

    if Form.validate_on_submit():
        Wo.update(Title= Form.Title.data,Meaning= Form.Meanging.data)
        flash('Yeah!')
        return redirect(url_for('Words_views.ones',T=Wo.Title))
    
    Form.Title.data=Wo.Title
    Form.Meaning.data=Wo.Meaning

    return render_template('change.html',title='Change-'+Wo.Title, Form = Form)