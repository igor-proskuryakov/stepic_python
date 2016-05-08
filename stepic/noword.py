st=[]
txt=[]
uniqtxt=[]
n = int(input())
for i in range(n):
    s = str(input())
    s = s.lower()
    if s not in st:
        st.append(s)
m = int(input())
for i in range(m):
     a = str(input()).split()
     for j in a:
         j=str(j).lower()
         if j not in uniqtxt:
            uniqtxt.append(j)
for i in uniqtxt:
    if i not in st:
        print(i)