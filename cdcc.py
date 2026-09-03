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

head = n1

# reverse
prev = None
curr = head

while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt

head = prev

# traversal
temp = head
while temp:
    print(temp.data)
    temp = temp.next