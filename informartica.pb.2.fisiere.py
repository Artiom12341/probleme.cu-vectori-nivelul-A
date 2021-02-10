m=['1','2','3','4','5','6','7','8','9','10']
s=1
if ((len(m)>=1) and (len(m)<=100)):
    for i in range(0, len(m)): 
        m[i] = int(m[i]) 
        s=s*m[i] 
print('produsul numarului=',s)
print("Suma cifrelor numarului=",sum(m))