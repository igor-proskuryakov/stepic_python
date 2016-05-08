ways = {'север':0,'юг':0,'запад':0,'восток':0}
n = int(input())
for i in range(n):
    d = str(input()).split()
    if d[0] in ways:
        ways[d[0]] += int(d[1])
k1 = ways['восток'] - ways['запад']
k2 = ways['север'] - ways['юг']
print(k1,k2,sep=' ')
