#coding : utf-8

from flask import render_template
from flask import Blueprint

main_views = Blueprint('main_views',__name__)

@main_views.route('/')
def index():
    return render_template('index.html',title=u'主页')