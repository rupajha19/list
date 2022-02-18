# Write a Python program to sort a given matrix in ascending order according to the sum of its rows.
#  Go to the editor
# Original Matrix:
# [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows
# [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
# Original Matrix:
# [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows
# [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
a=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
i=0
while i <len(a):
    j=0
    