s="()[{}()]"
pairs={')':'(', ']':'[', '}':'{'}
stacks=[]
for ch in s:
    if ch in "([{":
        stacks.append(ch)
    else:
        if not stacks or stacks[-1] != pairs[ch]:
            print("False")
            break
        stacks.pop()
else:
    print("True")