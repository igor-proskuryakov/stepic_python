a = int(input())
mat=[]
line=[]
b=1
for i in range(a):
    for j in range(a):
        line.append(0)
    mat.append(line)
    line=[]
print(mat)
istart=0
iend = a
jstart = 0
jend = a
for i in range(istart,iend):
    for j in range(jstart,jend):
       mat[i][j] = b
       b +=1
       if j == jend-1:
            jstart +=1
            istart +=1
            for i in range(istart,iend):
                mat[i][j] = b
                b+=1
for i in range(a):
    for j in range(a):
        print(mat[i][j],end=' ')
    print(end='\n')