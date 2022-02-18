l=[5,0,1,8,2,6,3,9,4,7]
for j in range(len(l)):
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            a=l[i]
            l[i]=l[i+1]
            l[i+1]=a
print(l)