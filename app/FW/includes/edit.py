# coding :utf-8

from FW.models import Units,Words

def trans_out(T):
    Lin = ''
    U = Units.objects(Title= T).first()

    for i in U.List:
        W = Words.objects(Title=i).first()
        Lin = Lin + str(W.Title) + "\n"
    
    return Lin

def trans_in(Lin,T):
    U = Units.objects(Title=T).first()

    L = U.List
    
    Lin = Lin.split('\r\n')

    Eor = []

    for i in Lin:
        title = i
        if Words.objects(Title=title).first() == None:
            Eor.append(title)
            continue
        if title not in L:
            L.append(title)
    
    U.update(List=L)
        
    return Eor