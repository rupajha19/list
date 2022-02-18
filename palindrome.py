a=['n','i','t','i','n']
i=0
b=[]
while i<len(a):
    b.append(a[i])
    i+=1
print(b)
if b==a or a==b:
    print("palindrome")
else:
    print("not palindrome")
    