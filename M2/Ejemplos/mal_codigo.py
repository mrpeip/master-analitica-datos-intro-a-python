"""
Supongamos que queremos procesar un archivo CSV con información de usuarios, 
calcular su edad media y guardar una lista con los nombres en mayúsculas.
"""
import csv
import datetime

def f(x):
    f = open(x)
    r = csv.reader(f)
    l = []
    s = 0
    c = 0
    for i in r:
        if i[1] != "birthdate":
            bd = i[1].split("-")
            y = int(bd[0])
            a = datetime.datetime.now().year - y
            s = s + a
            c = c + 1
            l.append(i[0].upper())
    print("avg age: ", s / c)
    f2 = open("names.txt","w")
    for i in l:
        f2.write(i+"\n")
    f2.close()
