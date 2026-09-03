class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# create nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

# connect nodes
n1.next = n2
n2.next = n3
n3.next = n4
head=n1
fast=head
slow=head
n=2
for i in range(n):
    fast=fast.next
while fast.next:
    fast=fast.next
    slow=slow.next
slow.next=slow.next.next
while head:
    print(head.data)
    head=head.next
    
a=[1,2,3]
print(len(a))