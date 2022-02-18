student_marks=[55,50,60,70,80,90,100]
length=len(student_marks)
index=0
total_marks=0
while index<len(student_marks):
    total_marks=student_marks[index]+total_marks
    index=index+1
print("total_marks" +str(total_marks))


