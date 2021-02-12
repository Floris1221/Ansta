from decimal import *


#@Florian Gaffke


def Code_generator(code1, code2):
    list = []
    code1 =int (code1.replace("-",""))
    code2 =int (code2.replace("-",""))
    for i in range(code1+1,code2):
        i = str(i)
        i="-".join([i[0:2],i[2:]])
        list.append(i)
    print(list)


def List_checker(inlist,nr):
    refset = set()
    for i in range(1,nr,1):
        refset.add(i)
    inset = set(inlist)
    outset = refset.difference(inset)
    outlist = list(outset)
    print(outlist)



def Decimal_generator():
    lista = []
    for i in range(20,60,5):
        lista.append(Decimal(i/10))
    print(lista)


Code_generator("79-900", "80-155")
List_checker([0,2,3,6,9],10)
Decimal_generator()