from random import randint,random

def getObjDict():    
    obj={'obj1':{'id':'obj1','name':'ТК 6-19','p1':[16*round(random(),2),'up'],'p2':randint(2,6),'t1':[randint(75,110),'down'],'t2':randint(40,55)},
    'obj2':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj3':{'id':'obj3','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj4':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj4'},
    'obj5':{'id':'obj5','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj6':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj6'},
    'obj7':{'id':'obj4','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj8':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj9':{'id':'obj5','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj10':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj11':{'id':'obj6','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj12':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj13':{'id':'obj7','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj14':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj15':{'id':'obj8','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj16':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj17':{'id':'obj9','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj18':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj19':{'id':'obj10','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':[randint(75,110),'up'],'t2':randint(40,55)},
    'obj20':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj21':{'id':'obj11','name':'ТК 6-19','p1':[randint(5,16),'down'],'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj22':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj23':{'id':'obj12','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj24':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj25':{'id':'obj13','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj26':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj27':{'id':'obj14','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj28':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj29':{'id':'obj15','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj30':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj31':{'id':'obj16','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj32':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj33':{'id':'obj17','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj34':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj35':{'id':'obj17','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj36':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj37':{'id':'obj1','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj38':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj39':{'id':'obj1','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj40':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj41':{'id':'obj1','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj42':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj43':{'id':'obj1','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj44':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj45':{'id':'obj1','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj46':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj47':{'id':'obj1','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj48':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj49':{'id':'obj1','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj50':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj51':{'id':'obj1','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj52':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj53':{'id':'obj1','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj54':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj55':{'id':'obj1','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj56':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj57':{'id':'obj1','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj58':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    'obj59':{'id':'obj1','name':'ТК 6-19','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55)},
    'obj60':{'name':'ТК 6-23а','p1':randint(5,16),'p2':randint(2,6),'t1':randint(75,110),'t2':randint(40,55),'id':'obj2'},
    }
    return obj

def foo():
    pass