def fact(n):
    res = 1
    for i in range(n+1):
        if i != 0:
            res *=i
    return res
def intro(n,k):
    if k > n or k < 0:
        return 0
    if k == 0:
        return 1
    res = (fact(n))/(fact(k)*(fact(n-k)))
    return res
n, k = map(int, input().split())
result = int(intro(n-1,k)+ intro(n-1,k-1))
print(result)