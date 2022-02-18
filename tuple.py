# a=("rupa","minakshi","priyankas","husna")
# i=0
# count=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if len( a[i])>j:
#             count+=1
#         j=j+1
#     print(len(a[i]),a[i])

#     i=i+1


a=["rupa","minakshi","priyankas","husna"]
i=0
max=a[i]
for i in a:
    if i<max:
        max=i
        print(max,len(i))
