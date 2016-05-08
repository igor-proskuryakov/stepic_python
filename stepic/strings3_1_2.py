s = str(input())
t = str(input())
count = 0
i = 0
a = 0
while True:
    a = s.find(t,i)
    if  a != -1:
        count+=1

        i = a+ 1
    else:
        break
print(count)
