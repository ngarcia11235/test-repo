import sys
import math
import gzip
import sqlite3
def main():
    filename=sys.argv[1]
    conn=sqlite3.connect(filename)
    cur=conn.cursor()
    cur1=conn.cursor()
    cur2=conn.cursor()
    bookdict=topic(cur,cur1)
def topic(cur,cur1):
    booktopics=[]
    nosect=[]
    for x in range(50):
        booktopics.append('')
    for row in cur.execute('SELECT * FROM text ORDER BY id'):
        sect=row[2]
        book=int(row[5])-1
        for row1 in cur1.execute('SELECT * FROM section ORDER BY id'):
            if row1[0]==sect:
                if sect not in nosect:
                    booktopics[book]+=row1[1]
                    booktopics[book]+=' '
                    nosect.append(sect)
    print('books read')
    newword=''
    v=0
    v1=-1
    allwords=[]
    for x in booktopics:
        wordlist=[]
        v1+=1
        for y in x:
            a=0
            v+=1
            if 64<ord(y)<91:
                a=1
                newword+=y
            if 96<ord(y)<123:
                a=1
                newword+=y
            if a==0:
                wordlist.append(newword)
                newword=''
        uword=[]
        for z in wordlist:
            while z in uword:
                uword.remove(z)
            uword.append(z)
        booktopics[v1]=uword
        for x in uword:
            while x in allwords:
                allwords.remove(x)
            allwords.append(x)
    #for x in range(50):
    #    print(x,'-'*15)
    #    print(booktopics[x])
    worf=[]
    for x in range(len(allwords)):
        worf.append([])
        for y in range(len(booktopics)):
            for z in booktopics[y]:
                if z==allwords[x]:
                    worf[x].append(y+1)
    v=-1
    removal=[]
    for x in worf:
        v+=1
        a2=0
        if len(x)==1:
            removal.insert(0,v)
            a2=1
        if len(x)>20:
            removal.insert(0,v)
            a2=1
        for y in range(len(x)-1):
            if a2==0:
                if (x[y+1]-x[y])>3:
                    removal.insert(0,v)
                    a2=1
    print(removal)
    for x in removal:
        allwords.pop(x)
        worf.pop(x)
    for x in range(len(allwords)):
        print(allwords[x],worf[x])
main()
