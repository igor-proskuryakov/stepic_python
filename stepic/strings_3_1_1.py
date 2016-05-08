s = str(input())
a = str(input())
b = str(input())
count = 0
if (((a in s) and (a == b)) or ((a in s) and (a in b))):
    print("Impossible")
else:
    while True:
        if a in s:
            s = s.replace(a, b)
            count += 1

        else:
            break
    print(count)
