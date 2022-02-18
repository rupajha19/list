a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
i=0
sum=0
while i<len(a):
    sum+=a[i]
    sum+=b[i]
    sum+=c[i]
    i+=1
print(sum)
