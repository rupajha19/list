a=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)

