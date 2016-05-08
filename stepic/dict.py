nums = []
num=['0','1','2','3','4','5','6','7','8','9']
let = []
nm = []
ind1 =True
ind2 =True
with open('data.txt', 'r') as inf:
    for i in inf:
        i=i.strip()
        for j in range(len(i)):
            nums.append(i[j])
for i in nums:
    if i in num:
        nm.append(i)
        let.append('#')
    else:
        let.append(i)
        nm.append('#')
for i in range(len(nm)):
    if i != len(nm)-1:
        if (nm[i] != '#'):
            if nm[i+1] != '#':
                nm[i] += nm[i+1]
                nm[i+1] = '#'
while ind1 == True:
    if '#' in let:
        a = let.index('#')
        del let[a]
    else:
        ind1 = False
while ind2 == True:
    if '#' in nm:
        a = nm.index('#')
        del nm[a]
    else:
        ind2 = False
for i in range(len(let)):
    print(let[i] * int(nm[i]),end='')

