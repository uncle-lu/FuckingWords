#coding:utf-8

from flask import Flask, Blueprint
from flask_bootstrap import Bootstrap
from flask_mongoengine import MongoEngine
from flask_nav import Nav
from flask_nav.elements import Navber, View

App = Flask('FW')
Boot_strap = Bootstrap()
Databases = MongoEngine()
nav = Nav()

Top = Navber('FuckingWords', 
    View('Home','app.index'),
    View('Units','U.index'),
    View('Words','W.index')
)

from app.view

def create_app():

    nav.register_element('top', Top)
    Boot_strap.init_app(App)
    nav.init_app(App)
    Databases.init_app(App)

    return App
