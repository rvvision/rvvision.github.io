import re
import time

c=0
##f=open("about-us.html","r",encoding="UTF-8")
##for x in f:
##    c=c+1
##print(c)
##f=open("about-us.html","r",encoding="UTF-8")
##for i in f:
##    g=re.findall('<!--.*?-->',i)
##    if g:
##        print(g)
##c=0
d=0
s=''
ff=0
f=open("about-us.html","r",encoding="UTF-8")        
for j in f:
    gg=0
    for i in j:
        if i=='<'and c==0:
            c=1
            gg=1
            print(c)
        if i=='!' and c==1:
            c=0
            gg=1
            ff=2
            print(c)
        if ff==2 and i == '-':
            c=3
            gg=1
            print(c)
        if c==3 and i == '-':
            c=4
            gg=0
            print(c)
        if c==4 and i=='-':
            c=5
            gg=1
            print(c)
        if c==5 and i == '-':
            c=6
            gg=1
            print(c)
        if c==6 and i == '>':
            c=0
            gg=0
            print(c)
        if gg==0 and c==0:
            s=s+i
            print (i)
        d=d+1

        
print(d)        
            
