incode = str(input())
decode = str(input())
strIncode = str(input())
strDecode = str(input())
result = []
result1=[]
code = {}
decod = {}
for i in range(len(decode)):
    decod[decode[i]]=incode[i]
for i in range(len(incode)):
    code[incode[i]]=decode[i]
for i in strIncode:
    if i in code.keys():
        result.append(code[i])
    else:
        result.append(i)
for i in strDecode:
    if i in decod.keys():
        result1.append(decod[i])
    else:
        result1.append(i)
for i in result:
    print(i,end="")
print(end="\n")
for i in result1:
    print(i,end="")