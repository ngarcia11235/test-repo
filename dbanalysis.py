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
    #text=getext(cur)
    #text=sectiontext(cur)
    #print('getext done')
    #bookdict=bookget(cur)
    #print('bookget done')
    #sectdict=sectget(cur)
    #passdict=passdict(cur)
    #dewytext=dewy(cur,cur1,cur2)
    #sectlen(cur)
    words=clearn(text)
    #words=nonfiller(words)
    word3=words.copy()
    print("clern done")
    worf=freq(word3)
    print('worf done')
    #nve=entropy(worf,words)
    #cfc=compcalc(words)
    #print('({},{})'.format(nve,cfc))
def getext(cur):
    # extracts and returns text from database
    s=''
    for row in cur.execute('SELECT * FROM text ORDER BY book_no'):
        s+=row[1]
        s+=' '
    return s
def sectiontext(cur):
    text=''
    for x in cur.execute('SELECT * FROM section ORDER BY id'):
        text+=x[1]
        text+=' '
    return text
def bookget(cur):
    # returns a list of the books and the sections contained within each
    x=0
    seclist=[]
    booklist=[]
    for row in cur.execute('SELECT * FROM text ORDER BY book_no'):
        x1=row[4]
        seclist.append(row[2])
        if x1!=x:
            x=x1
            y1=[]
            for y in seclist:
                y1.append(y)
            for i in y1:
                while i in seclist:
                    seclist.remove(i)
                seclist.append(i)
            z={'book':x1,'topic': 'placeholder','sections':seclist}
            booklist.append(z)
            seclist=[]
    return booklist
def dewy(cur,cur1,cur2):
    dgdew=[]
    jrdew=[]
    for row in cur.execute('SELECT * FROM text ORDER BY text'):
        num=0
        num+=row[8]
        num+=row[7]*100
        num+=row[6]*100000
        num+=row[5]*100000000
        num+=10000000000
        if num>20000000000:
            print('its over 9000')
        dgdew.append(num)
    for row in cur.execute('SELECT * FROM text ORDER BY text'):
        num=0
        num+=row[0]
        n=row[10]
        for row1 in cur1.execute('SELECT * FROM book ORDER BY id'):
            
            if row1[0]==n:
                num+=row1[2]*100000
                num+=row1[1]*10000000
                n=row1[1]
                for row2 in cur2.execute('SELECT * FROM work ORDER BY id'):
                    if row2[0]==n:
                        num+=row2[1]*10000000000
        num+=1000000000000
        if num>2000000000000:
            print('its over 9000')
        jrdew.append(num)
def sectlen(cur):
    n=0
    n1=0
    lengths=[]
    for row in cur.execute('SELECT * FROM section ORDER BY id'):
        n1=n
        n=row[2]
        if n>0:
            lengths.append(n-n1)
    print(lengths)
def clearn(text):
    # cleans up the input and returns a more usable text
    newword=''
    wordlist=[]
    v=0
    for x in text:
        a=0
        v+=1
        if 64<ord(x)<91:
            a=1
            newword+=x
        if 96<ord(x)<123:
            a=1
            newword+=x
        if a==0:
            wordlist.append(newword)
            newword=''
    return wordlist
def nonfiller(words):
    fillerlist=['et','de','ad','a','ab','cui','cum','ei','eius','eo','eorum','erit','pro','qui','quid','quibus','quam','quinquennium','quinque','quisque','ne','plus','post','vel','ut']
    for x in fillerlist:
        while x in words:
            words.remove(x)
    return words
def freq(word3):
    # does a frequency analysis on the words and returns a list of unique words + frequencies
    uwords=[]
    wordf=[]
    word3.sort()
    word2=word3.copy()
    num=0
    breaker=0
    for x in range(len(word3)):
        n=0
        uwords.append(word3[0])
        y=word3[0]
        a=0
        while a==0:
            if len(word3)>0:
                if word3[0]==y:
                    word3.pop(0)
                else:
                    a=1
            else:
                print("100% done")
                breaker=1
                a=1
            n+=1
        wordf.append(n)
        if breaker==1:
            for x in range(len(uwords)):
                print(uwords[x],wordf[x])
            word3=word2.copy()
            return wordf
def entropy(worf,words):
    # does  entropy calculation and returns normalized shannon entropy
    wordent=[]
    shanent=0
    normshanent=0
    for x in worf:
        y=x/len(words)
        z=-y*(math.log2(y))
        wordent.append(z)
    for x in wordent:
        shanent+=x
        normshanent+=x/math.log2(len(worf))
    print('shannon entropy: {}'.format(shanent))
    print('normalized shannon entopy: {}'.format(normshanent))
    return normshanent
def compcalc(words):
    # compresses the text and returns compression factor
    x=''
    for y in words:
        x+=y
        x+=' '
    bytx=x.encode()
    lenword=len(bytx)
    lencomp=len(gzip.compress(bytx))
    compfact=lenword/lencomp
    print(bytx)
    print(gzip.compress(bytx))
    print('text length: {}'.format(lenword))
    print('compressed text length: {}'.format(lencomp))
    print('compression factor: {}'.format(compfact))
    return compfact
main()
#(0.7319206157067065,3.1043677046960734)
(0.7319206157067065,3.1043677046960734)
