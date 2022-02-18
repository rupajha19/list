a=[3,5,6,8,12,34,5,67,8]
i=0
min=a[0]
while i<len(a):
    if a[i]<min:
        min=a[i]
    i+=1
print(min)