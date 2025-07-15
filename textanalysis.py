import sys
import math
import gzip
filename=sys.argv[1]
def main():
    text=open(filename,'r')
    print(text)
    words=clearn(text)
    print("clern done")
    worf=freq(words)
    print('worf done')
    nve=entropy(worf,words)
    cfc=compcalc(words)
    print('({},{})'.format(nve,cfc))
def clearn(text):
    newword=''
    wordlist=[]
    for x in text.read():
        a=0
        if 64<ord(x)<91:
            a=1
            newword+=x
        if 96<ord(x)<123:
            a=1
            newword+=x
        if ord(x)in[39,44]:
            a=1
            newword+="'"
        if a==0:
            wordlist.append(newword)
            newword=''
    while '' in wordlist:
        wordlist.remove('')
    print("spaces cleared")
    return wordlist
def freq(words):
    uwords=[]
    wordf=[]
    print("02")
    for x in words:
        n=0
        a=0
        for y in uwords:
            if x==y:
                wordf[n]+=1
                a=1
            n+=1
        if a==0:
            uwords.append(x)
            wordf.append(1)
    for x in range(len(uwords)):
        print(uwords[x],wordf[x])
    print(uwords)
    return wordf
def entropy(worf,words):
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
