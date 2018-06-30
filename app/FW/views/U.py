#coding:utf-8

from flask import render_template, redirect, url_for, flash, request, abort
from FW.models import Units,Words
from FW.forms import UnitsForm, CreateForm
from FW.includes.edit import trans_in, trans_out

from . import Units_views

@Units_views.route('/', methods=['GET', 'POST'])
def index():
    page = 1
    page = int(request.args.get('page','1'))
    
    skip_number= (page-1)*25

    Lis = Units.objects.order_by('-create_at').skip(skip_number).limit(25)

    p = int(Units.objects.count() / 25)

    return render_template('U/index.html',title='Units',L = Lis,page= page,p =p)

@Units_views.route('/<string:T>',methods=['GET','POST'])
def ones(T):

    U = Units.objects(Title=T).first()

    Woli = U.List
    Li = []

    for i in Woli:
        l = Words.objects(Title=i).first()
        Li.append({
            'Title':l.Title,
            'Meaning':l.Meaning
            })
    
    return render_template('U/ones.html',title=T, L = Li)

@Units_views.route('/<string:T>/delete/<string:N>')
def delete(T,N):

    U = Units.objects(Title=T).first()

    if U == None:
        abort(404)
    
    if N in U.List:
        try:
            L = U.List
            L.remove(N)
            U.update(List=L)
            flash('Success!')
        except:
            flash('Fail!')
    else:
        abort(404)
    
    return redirect(url_for('Units_views.ones',T=T))

@Units_views.route('/<string:T>/Editor',methods=['GET','POST'])
def edit(T):
    
    U = Units.objects(Title=T).first()

    if U == None:
        abort(404)
    
    F = UnitsForm()

    if F.validate_on_submit():
        Eor = trans_in(F.Introduction.data,T)
        if Eor :
            flash(u'以下词汇不存在词库中,请先批量加入词库中,\n %s' % Eor)
        return redirect(url_for('Units_views.ones',T=T))
        
    F.Introduction.data = str(trans_out(T))

    return render_template('U/editor.html',title=T,F = F)

@Units_views.route('/create',methods=['GET','POST'])
def create():

    F = CreateForm()

    if F.validate_on_submit():
        U = Units(Title= F.Title.data)
        U.save()
        flash('Yeah!')
        return redirect(url_for('Units_views.ones',T=F.Title.data))

    return render_template('U/create.html',title=u'Create New',F = F)

@Units_views.route('/rename/<string:T>',methods=['GET','POST'])
def rename(T):
    F = CreateForm()

    U = Units.objects(Title=T).first()
    if U == None:
        abort(404)
    
    if F.validate_on_submit():
        U.update(Title = F.Title.data )
        flash('Yeah!')
        return redirect(url_for('Units_views.ones',T=F.Title.data))
    
    F.Title.data = U.Title

    return render_template('U/create.html',title='Rename',F=F)