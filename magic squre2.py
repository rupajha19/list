magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]

i=0
while i<len(magic_square):
        j=0
        sum=0
        while j<len(magic_square[i]):
            sum=sum+(magic_square[i][j])
            j=j+1
        print(sum)
        i=i+1



