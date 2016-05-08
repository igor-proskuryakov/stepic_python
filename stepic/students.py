classes={}
students={}
for i in range(1,12):
    classes[i]=0
    students[i]=0
with open('data.txt','r') as tb:
    for line in tb:
        d = line.split()
        classes[int(d[0])] += int(d[2])
        students[int(d[0])] +=1

with open('result.txt','w') as res:
    for i in classes.keys():
        if classes[i] != 0:
            j =classes[i] / students[i]
        else:
            j = '-'
        s = str(i)+' '+str(j)+'\n'
        res.write(s)
