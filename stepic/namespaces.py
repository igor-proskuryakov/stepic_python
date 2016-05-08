n = int(input())
result = []
a={'global':{'parent':0,'variables':[]}}
def add(n,v):
    global a
    b = a[n]
    b['variables'].append(v)
def create(nch,np):
    global a
    if nch not in a.keys() :
        a[nch] = {'parent':np,'variables':[]}
def get(n,v):
    global a
    b = a[n]
    count =1
    while  count != 0:
        if v in b['variables']:
            return n
        elif b['parent'] == 0:
            return 'None'
        else:
            n = b['parent']
            b = a[n]



for i in range(n):
    string = input().split()
    func = string[0]
    namespace = string[1]
    variable = string[2]
    if func == 'add':
        add(namespace,variable)
    elif func == 'create':
        create(namespace,variable)
    elif func == 'get':
        result.append(get(namespace,variable))
for i in result:
    print(i)


