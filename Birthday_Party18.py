a=list(input())
c=[]
for i in a:
    if i not in c and i !=",":
        c.append(i)
print(len(c))        