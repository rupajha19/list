list=[1,-2,3,-4,5,-6,-7,-8,9,-10]
n_c=0
p_c=0

# for i in list:
#     if i>=0:
#         p_c+=1
#     else:
#         n_c+=1
    
# print("positive number",p_c)
# print("negative number",n_c)
i=0
while i<len(list):
    if n_c[i]<=0:
        n_c+=1
    else:
        p_c+=1
    i+=1
print("positive number",p_c)
print("negative number",n_c)

