#coding:utf-8

from flask import Blueprint

Words_views = Blueprint('Words_views',__name__)

Units_views = Blueprint('Units_views',__name__)

Create_pdf_views = Blueprint('Create_pdf_views',__name__)

from FW.views import W
from FW.views import U
from FW.views import C