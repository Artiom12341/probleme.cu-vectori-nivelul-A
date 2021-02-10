import math
#problema nr.3 nivel A
m=['1','2','3','4','5','6','7','8','9','10']
s=0
c=0
d=0
f=0
g=0
h=0
if ((len(m)>=1) and (len(m)<=100)):
    for i in range(0, len(m)): 
        if int(m[i])<0:
            s=s+1
        if int(m[i])%2==0:
            c=c+1
        if m[i]!=0:
            d=d+1
        if ((int(m[i])%3==0) and (int(m[i])%5==0)):
            f=f+1
        if ((int(m[i])%7==0) or (int(m[i])%9==0) or (int(m[i])%11==0) ):
            g=g+1
        if math.sqrt(int(m[i]))>3:
            h=h+1
print(s,c,d,f,g,h)
