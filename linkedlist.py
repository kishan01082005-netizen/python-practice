# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# # create nodes
# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)

# # connect nodes
# n1.next = n2
# n2.next = n3

# # traversal
# count=0
# temp = n1
# while temp:
#     count+=1
#     print(temp.data)
#     temp = temp.next

# # print(count)
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# # create nodes
# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)

# # connect nodes
# n1.next = n2
# n2.next = n3

# # newnode=Node(40)
# # head=n1
# # newnode.next=head
# # head=newnode

# # temp=head
# # while temp:
# #     print(temp.data)
# #     temp=temp.next
# target=20
# temp=n1
# while temp:
#     if temp.data==target:
#         print ("found")
#         break
#     else:
#         temp=temp.next
        
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# # create nodes
# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)

# # connect nodes
      temp=temp.next
        
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

temp=n1
while temp:
    if temp.next==None:
        temp.next=newnode
        break
    temp=temp.next
temp=n1
while temp:
    print(temp.data)
    temp=temp.next
