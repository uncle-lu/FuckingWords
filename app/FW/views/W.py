# coding : utf-8

from flask import render_template, redirect, url_for, flash, request, abort
from FW.models import Words
from FW.forms import WordsForm , TextForm
from FW.includes.entry import enter
from . import Words_views

@Words_views.route('/', methods=['GET', 'POST'])
def index():
    page = 1

    page = int(request.args.get('page', '1'))

    skip_num=(page-1)*25
    
    Lis = Words.objects.order_by('+create_at').skip(skip_num).limit(25)

    p = int(Words.objects.count() / 25 + 0.5)

    return render_template('W/index.html',title= 'Words',L = Lis, page= page ,p = p)

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

    return render_template('W/change.html',title='Change-'+Wo.Title, Form = Form)

@Words_views.route('/Add',methods=['GET','POST'])
def add():

    F = TextForm()

    if F.validate_on_submit():
        enter(F.Introduction.data)
        return redirect(url_for('Words_views.index',page=1))
    
    return render_template('W/add.html',title=u'新加入',F = F)
