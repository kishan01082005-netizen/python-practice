arr=[1,2,3,-1,4,3,-8]
pos=[]
neg=[]
for i in range (len(arr)):
    if arr[i]>0:
        pos.append(arr[i])
    else:
        neg.append(arr[i])
result=[]
i=0
j=0
while i<len(pos) and j<len(neg):
    result.append(pos[i])
    result.append(neg[j])
    i+=1
    j+=1 
while i<len(pos):
    result.append(pos[i])
    i+=1
print(result)