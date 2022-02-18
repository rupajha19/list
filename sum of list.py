# num=[1,2,3,4,5,6,7,8,9,10]
# i=0
# sum=0
# while i <len(num):
#     sum=sum+num[i]
#     i=i+1
# print(sum)


a=[1,2,3,4,5]
b=[1,2,1,1,4,6]

c=[]
for i in a:
    if i in b:
        c.append(i)
print(c)


