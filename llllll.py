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
head=n1
slow=head
fast=head
while fast and fast.next:
    slow=slow.next
    fast=fast.next.next
print(slow.data)