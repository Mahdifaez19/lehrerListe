#!/usr/bin/env python3
import requests
from datetime import datetime
from threading import Timer

def listenSplit(List, Zeichen):
    endListe = []
    y = []
    woerterbuch = {}
    for i in List:
        zwischenListe =  i.split(Zeichen)
        if(len(zwischenListe)<2) :
            break
        else:
            zwischenListe[1] = zwischenListe[1][:-1]
            woerterbuch[zwischenListe[0]] = zwischenListe[1]
    return woerterbuch
#    for x in endListe:
#        if(not y):
#            y = x
#        else:
#            res = mergeList(y,x)
#            y = []
    return endListe
    
def mergeList(List1,List2):
    for i in List2:
        List1.append(i)
    return List1

def zeileDurchsuchen(datei):
    zeile = 0
    gefunden = False
    anfang = 0
    ende = 0
    for line in datei:
        zeile = zeile +1
        for buchstaben in line:
            if (buchstaben == "(" and gefunden == False):
#               print("(")
                gefunden = True
                anfang = zeile
            if (buchstaben == ")"):
                ende = zeile
#    print("Anfang: " + str(anfang))
#    print("Ende: " + str(ende))
#    print("Zeile: " + str(zeile))
    res = [anfang,ende]
    return res





import os
import requests
import json

def main():

    url = 'http://reismann.lspb.de/Verwaltung/stundenplaene/showlezi1.php?code=lmkjnsdfkljbn2480fnsdj982hujngvb8u0jo2nl54rv890bjik243lvdjin4235078ulnvs&type=2'
    r = requests.get(url, allow_redirects=True)
    open('board.pdf', 'wb').write(r.content)

    #os.system('pip install pdfminer')
    #os.system('cd /home/mahdi/anaconda3/bin')
    cmd = 'python /home/mahdi/anaconda3/bin/pdf2txt.py /home/mahdi/Documents/VertretungsstundenAusfallen/board.pdf > out_file.txt'
    os.system(cmd)

    daten = open("out_file.txt")
    daten2 = open("out_file.txt")
    zeile = zeileDurchsuchen(daten2)
    zeilenListe = []
    LehrerListe = {}
    splitListe = []
    i = 0
    #print(zeile[0])
    #print(zeile[1])
    for line in daten:
        i = i +1    
        if(i >= zeile[0] and i <= zeile[1]):
            splitListe.append(line.split())
            zeilenListe.append(line)
    #print(splitListe)
    count = 0
    endListe = []
    for x in splitListe:
        if(count < len(splitListe)):
            endListe = mergeList(endListe,splitListe[count])
        count = count +1
    #print("Endliste: ")
    #print(endListe)
    #print(zeilenListe)
    LehrerListe = listenSplit(endListe,"(")        
    #print(LehrerListe)
    with open('db.json', 'w') as json_file:
        json.dump(LehrerListe, json_file)
    #res = zeileDurchsuchen(daten)
    #print(res[0])
    print(LehrerListe)
    r = requests.post("https://my-json-server.typicode.com/Mahdifaez19/lehrerListe/db", data=LehrerListe)
    response = requests.get("https://my-json-server.typicode.com/Mahdifaez19/lehrerListe/db")
    print(response)
    daten2.close()
    daten.close()


x=datetime.today()
y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

t = Timer(secs, main())
#t.start()
main()