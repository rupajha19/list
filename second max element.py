a=[]
# size=int(input("enter size of list::"))
# for i in range(size):
#     val=int(input("enter number::"))
#     a.append(val)
# maxval=max(a)
# print("first max value in the list=::",maxval)
# a.remove(maxval)
# smax=max(a)
# print("second max value in the list is::",smax)

n=int(input("enter rows::"))
i=1
while n>0:
    b=1
    while b<i:
        print(" ",end="")
        b=b+1
    j=1
    while j<=(n*2)-1:
        print(b,end="")
        j=j+1
    print()
    n=n-1
    i=i+1
    

    