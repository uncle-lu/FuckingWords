#coding : utf-8

from FW.models import Words, Units
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

class TextForm(FlaskForm):
    Introduction = TextAreaField(u'编辑框', validators=[Required()])
    Submit = SubmitField('Submit!')

class CreateForm(FlaskForm):
    Title = StringField('Name',validators=[Required()])
    Submit = SubmitField('Submit!')

class Create_pdfForm(FlaskForm):
    Units_list = StringField(u'生成Units列表',validators=[Required()])
    Words_count = StringField(u'生成单词数',validators=[Required()])
    Submit = SubmitField('Submit!')

    def validate_Units_list(self,field):
        l = field.data.split(',')
        for i in l:
            if Units.objects(Title=i).first() == None:
                return ValidationError("Can't find %s in database" % i)
    
    def validate_Words_count(self,field):
        if int(field.data) > 80:
            return ValidationError(u"不能生成超过80的单词听写纸")