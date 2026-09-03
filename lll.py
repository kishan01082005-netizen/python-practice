class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# create nodes
n1 = Node(10)

n2 = Node(20)
n3 = Node(30)

# connect nodes
n1.next = n2
n2.next = n3
newnode=Node(40)
k=1
count=1
temp=n1
while temp:
    if(count==k):
        newnode.next=temp.next
        temp.next=newnode
        break
    temp=temp.next
    count+=1
temp=n1
while temp:
    print(temp.data)
    temp=temp.next