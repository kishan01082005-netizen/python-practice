arr=[3,1,-2,-5,2,-4]
pos=0
neg=1
ans=[0]*len(arr)
for i in range(len(arr)):
    if arr[i]>0:
        ans[pos]=arr[i]
        pos+=2
    elif arr[i]<0:
        ans[neg]=arr[i]
        neg+=2
print(ans)

