n = int(input())
classes ={}
for i in range(n):
    s = input().split(' ')
    print(s)

    if s[0] not in classes.keys() and s[0] != ':':
        classes[s[0]]={'parent':[]}
    obj = classes[s[0]]
    for j in range(1,(len(s))):
        if s[j] != ':':
            obj['parent'].append(s[j])

for i in classes.keys():
    item = classes[i]
    #print(i,":",item)
    for j in item['parent']:
        object = classes[j]
        if object['parent'] != []:
            item['parent'].extend(object['parent'])
    classes[i] = item
#print(classes)
k = int(input())
for i in range(k):
    r = input().split(' ')
    if r[1] in classes.keys():
        if r[0] != r[1]:
            p = classes[r[1]]
            #print(r[1],':',p)
            par = r[0]
            if par in p['parent']:
                print('Yes')
            else:
                print('No')
        else:
            print('Yes')
    else:
        print('No')






