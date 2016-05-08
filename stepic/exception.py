n = int(input())
ex = {}
for i in range(n):
    s = input().split()
    if len(s) > 2:
        for f in range(2, len(s)):
            if s[f] not in ex.keys():
                ex[s[f]] = []
                obj = ex[s[f]]
                obj.append(s[0])
            ex[s[f]].append(s[0])
    else:
        if s[0] not in ex.keys():
            ex[s[0]] =[]
r=[]
for i in ex.keys():
    for j in ex[i]:
        if j in ex.keys():
            r.extend(ex[j])
        ex[i].extend(r)
        r=[]
m = int(input())
res = []
exp = []
for i in range(m):
    t = input()
    if t not in res:
        if t in ex.keys():
            res.extend(ex[t])
        else:
            res.append(t)
    else:
        exp.append(t)
for i in exp:
    print(i)
