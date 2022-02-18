magic_square = [
    [5, 3, 7],
    [1, 8, 9],
    [6, 4, 2]
]
 
i=0
while i<len (magic_square):
    j=0
    sum=0
    while j<len(magic_square[i]):
        sum=sum+(magic_square[i][j])
        j=j+1
    print(sum)
    i=i+1
print("its magic squre")