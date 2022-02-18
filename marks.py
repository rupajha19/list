marks=[30,33,50,66,33,70,60,48,90]
length=len(marks)
index=0
less_than50=0
more_than50=0
while index<len[marks]:
    while index<length:
        marks = marks(index)
    if marks < 50:
        less_than50 = less_than50 + 1
    else:
        more_than50 = more_than50 + 1
        index = index + 1
print("less_than50::"+ str(less_than50))
print("more_than50::"+ str(more_than50))
