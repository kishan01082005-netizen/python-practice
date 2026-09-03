inpu=[5,3,7]
mainstack=[]
minstack=[]
for k in inpu:
    if not mainstack:
        mainstack.append(k)
        minstack.append(k)
    elif k<minstack[-1]:
        mainstack.append(k)
        minstack.append(k)
    else:
        mainstack.append(k)
        minstack.append(minstack[-1])
        
print(minstack[-1])
    