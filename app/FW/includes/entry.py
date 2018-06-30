# coding:utf-8

from FW.models import Words

def enter(Len):
    
    Len = str(Len)
    Len = Len.split('\r\n')
    print(Len)
    
    for group in Len:
        group = group.split('|')

        print(group)
        Wo = Words.objects(Title=group[0]).first()
        if Wo != None:
            Wo.update(Meaning=group[1])
            continue
        Wo = Words(Title = group[0],Meaning = group[1])
        Wo.save()
    
    return 