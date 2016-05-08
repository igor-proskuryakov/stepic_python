m=[]
b=''
s=[]
d=[]
while b != 'end':
    a = str(input()).split()
    m.append(a)
    b=a[0]
del m[-1]
for i in range(len(m)):
    for j in range(len(m[i])):
        if i == (len(m)-1):
            p = 0
        else:
            p = i +1
        if j == (len(m[i])-1):
            t = 0
        else:
            t= j+1
        n = int(m[i-1][j]) + int(m[p][j]) + int(m[i][j-1]) + int(m[i][t])
        s.append(n)
    d.append(s)
    s=[]
for i in range(len(d)):
    for j in range(len(d[i])):
        print(d[i][j],end=' ')
    print(end='\n')




