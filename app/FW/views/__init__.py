#coding:utf-8

from flask import Blueprint

Words_views = Blueprint('Words_views',__name__)

Units_views = Blueprint('Units_views',__name__)

from app.views import W
from app.views import U