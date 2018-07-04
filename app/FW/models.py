#coding : utf-8

from FW.app import Databases

class Words(Databases.Document):
    Title = Databases.StringField(required= True)
    Meaning = Databases.StringField(required= True)

class Units(Databases.Document):
    Title = Databases.StringField(required= True)
    List = Databases.ListField( Databases.StringField(required= True))

class Pdfs(Databases.Document):
    Id = Databases.IntField(required=True)
    Title = Databases.StringField(required= True)
    File = Databases.FileField(required= True)