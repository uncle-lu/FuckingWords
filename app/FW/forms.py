#coding : utf-8

from app.models import Words, Units
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms import ValidationError
from wtforms.validators import Required

class WordsForm(FlaskForm):
    Title = StringField(u'本体', validators=[Required()])
    Meaning = StringField(u'解释', validators=[Required()])
    Submit = SubmitField('Submit!')
    
class UnitsForm(FlaskForm):
    Introduction = TextAreaField(u'本单元核心编码', validators=[Required()])
    Submit = SubmitField('Submit!')