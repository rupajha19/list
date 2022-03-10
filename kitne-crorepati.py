kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
count1=0
i=0
while i<len(kitna_paisa_hai):
    if kitna_paisa_hai[i]>=10000000:
        count1+=1
    i+=1
print(count1,"carorpati hai")
count2=0
j=0
while j<len(kitna_paisa_hai):
    if kitna_paisa_hai[j]>=100000:
        count2+=1
    j+=1
print(count2,"lakhpati hai")
count3=0
k=0
while k<len(kitna_paisa_hai):
    if kitna_paisa_hai[k]<100000:
        count3+=1 
    k+=1
print(count3,"dilwaale")