a=[]
size=int(input("how many elemet you want::"))
for i in range(size):
    val=int(input("enter number::"))
    a.append(val)
sum=0
for i in range(size):
    sum=sum+a[i]
print("sum of element=",sum)

