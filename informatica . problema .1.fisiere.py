m=['1','2','3','4']
if ((len(m)>=10) and (len(m)<=100)):
    print(m[2:3],m[3:4],m[9:10])
    b=(int(str(m[2]))+int(str(m[3]))+int(str(m[8])))
    print(b)
    print(int(str(m[0]))+int(5),int(str(m[-1]))+int(5))
    print(int(str(m[4]))-int(10),int(str(m[5]))-int(10))
else:
    print('modifica vectorul')