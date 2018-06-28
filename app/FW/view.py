#coding : utf-8

from flask import render_template
from FW.app import App

@App.route('/')
def index():
    render_template('index.html')