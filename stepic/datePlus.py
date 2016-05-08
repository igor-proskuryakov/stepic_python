import datetime
a = input().split()
b = int(input())
d = datetime.date(int(a[0]), int(a[1]) ,int(a[2]))

t = datetime.timedelta(days = b)
c = d +t
print(c.year,c.month,c.day)