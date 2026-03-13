s=(()())(())(()(()))
count=0
for ch in s:
    if ch =='(':
        if count>0:
            count+=1
    else:
        count-=1
        ans=count
print(count)
    
