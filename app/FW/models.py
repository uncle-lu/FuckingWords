#coding : utf-8

from FW.app import Databases

class Words(Databases.Document):
    Title = Database.StringField(required= True)
    Meaning = Database.StringField(required= True)

class Units(Databases.Document):
    List = Databases.ListField( Databases.StringField(required= True))