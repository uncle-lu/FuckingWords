#coding:utf-8

from flask import Flask, Blueprint
from flask_bootstrap import Bootstrap
from flask_mongoengine import MongoEngine
from flask_nav import Nav
from flask_nav.elements import View, Navbar
from FW.config import config

Databases = MongoEngine()
bootstrap = Bootstrap()
nav = Nav()

Top = Navbar('FuckingWords', 
    View('Home','main_views.index'),
    View('Units','Units_views.index'),
    View('Words','Words_views.index')
)

def create_app():

    App = Flask(__name__)
    App.config.from_object(config['debug'])

    Databases.init_app(App)
    bootstrap.init_app(App)
    nav.init_app(App)
    nav.register_element('top', Top)

    from FW.views import Units_views, Words_views,Create_pdf_views
    from FW.view import main_views

    App.register_blueprint(main_views)
    App.register_blueprint(Units_views,url_prefix='/Units')
    App.register_blueprint(Words_views,url_prefix='/Words')
    App.register_blueprint(Create_pdf_views,url_prefix='/C_pdfs')

    return App