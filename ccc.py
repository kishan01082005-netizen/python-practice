# a=[1,0,2,3,0,0,4,5,1]
# temp=[]
# k=[]
# for i in a: 
#     if a[i]!=0:
#         temp.append(a[i])
#     elif a[i]==0:
#         k.append(a[i])
# a=temp+k
# print(a)
    
# a=[0,23,4,3,23,0,0,34]
# j=0

# for i in range(len(a)):
#     if a[i]!=0:
#         a[j]=a[i]
#         j+=1
        
# while j<len(a):
#     a[j]=0
#     j+=1
# print(a)  

#linear search 

# def a():
#     arr=[1,2,3,4,5]
#     num=3
#     for i in range (len(arr)):
#         if arr[i]==num:
#             return i
#     return -1
# print(a())

# def func():
#     a=[4,3,2,1]
#     for i in range(len(a)-1):
#         if a[i+1]<a[i]:
#             a[i],a[i+1]=a[i+1],a[i]                   
    
    
#     flag=1
#     for j in a:
#          if j==flag:
#              flag+=1
#     return flag
# print(func())

# arr=[1,2,2,3,3,4,4]
# for i in range(len(arr)):
#     count=0
#     num=arr[i]
#     for j in range(len(arr)):
#         if arr[j]==num:
#             count+=1
#     if count==1:
#         print(num)
# sum=0
# k=3
# maxlength=0
# arr=[1,2,3,1,1,1,1,4,2,3]
# for i in range(len(arr)):
#     sum=0
#     for j in range(i,len(arr)):
#         sum+=arr[j]
#         if sum==k:
#             cl=j-i+1
#             if cl>maxlength:
#                 maxlength=cl
# print(maxlength)

# target=14
# arr =[2,6,5,8,11]
# found=False
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]+arr[j]==target:
#             print("yes")
#             found=True
#             break
#     if found:
#         break
# if not found:
#     print("no")


# target=14
# arr=[2,6,5,8,11]
# r=set()
# for i in range(len(arr)):
#     if target-arr[i] in r:
#        print("pair found")
#        break
#     else:
#        r.add(arr[i])
       
# arr=[2,6,5,8,11]
# target=14
# num_index={}
# for i,num in enumerate(arr):
#     complement = target-num
#     if complement in num_index:
#         print("found",[num_index[complement],i])
#         break
#     num_index[num] = i


# arr=[2,1,1,1,1,2,2]
# freq={}
# for num in arr:
#     freq[num]=freq.get(num,0)+1
# print(max(freq,key=freq.get))
    
# arr=[2,1,1,1,1,1,2,2,2]
# count=0
# candidate=None

# for num in arr:
#     if count==0:
#         candidate=num
        
#     if num==candidate:
#         count+=1
#     else:
#         count-=1
        
# print(candidate)
    

# arr=[-2,-3,4,-1,-2,1,5,-3]
# maxi=arr[0]
# sum=0
# for i in range (len(arr)):
#         sum+=arr[i]
#         maxi=max(maxi,sum)
#         if sum<0:
#             sum=0
# print(maxi)

# arr=[]
# a=[0]*len(arr)
# posindex=0
# negindex=1
# for i in range(len(arr)):
#     if arr[i]>0:
#         a[posindex]=arr[i]
#         posindex+=2
#     else:
#         a[negindex]=arr[i]
#         negindex+=2
# print(a)
                
# ar=[1,2,-4,-5,3,4]
# a=[]
# b=[]
# result=[]
# for num in ar:
#     if num>0:
#         a.append(num)
#     else:
#         b.append(num)
# result=[]
# i=0
# j=0

# while i<len(a) and j<len(b):
#     result.append(a[i])
#     result.append(b[j])
#     i+=1
#     j+=1
    
        
# while i<len(a):
#     result.append(a[i])
#     i+=1
    
# while j < len(b):
#     result.append(b[j])
#     j += 1
# print(result)  


# arr=[7,1,5,3,6,4] 
# mini=arr[0]
# profit=0
# for i in range(len(arr)):
#     cost=arr[i]-mini
#     profit=max(cost,profit) 
#     mini = min(mini,arr[i])
# print(profit) 

# arr=[10,22,12,3,0,6]
# leader=[]
# maxi=0
# for i in range(len(arr),-1):
#     if arr[i]>maxi:
#         maxi=arr[i]
# print(maxi)

# arr=[13,46,24,52,20,9]
# for i in range(len(arr)):
#     minindex=i
#     for j in range(i+1,len(arr)):
#         if arr[j]<arr[minindex]:
#             minindex=j
#     arr[i],arr[minindex]=arr[minindex],arr[i]
# print(arr)       
         
#bubble sort

# arr=[13,46,24,52,20,9]
# swapped=True
# while swapped:
#     swapped=False
#     for i in range(len(arr)-1):
#         if arr[i]>arr[i+1]:
#             arr[i],arr[i+1]=arr[i+1],arr[i]
#             swapped=True
# print(arr)

# arr=[13,46,24,52,20,9]
# for i in range(1,len(arr)):
#     key=arr[i]
#     j=i-1
#     while j>=0 and arr[j]>key:
#         arr[j+1]=arr[j]
#         j-=1
#     arr[j+1]=key
# print(arr)



# arr=[10,22,13,4,56,54]
# leader=[]
# for i in range(len(arr)):
#     count=0
#     for j in range(i+1,len(arr)):
#         if arr[i]>arr[j]:
#             count+=1
    
#     if count == len(arr)-i-1:
#         leader.append(arr[i])
# print(leader)


# arr=[10,22,34,32,21]
# leader=[]
# maxi=arr[-1]
# leader.append(maxi)
# for i in range(len(arr)-2,-1,-1):
#     if arr[i]>maxi:
#         leader.append(arr[i])
#         maxi=arr[i]
# leader.reverse()
# print(leader)

# arr=[102,4,100,1,101,3,2,1,1]
# k=True
# while k:
#     k=False
#     for i in range(len(arr)-1):
#         count=0
#         if arr[i]>arr[i+1]:
#             arr[i],arr[i+1]=arr[i+1],arr[i]
#             k=True
# print(arr)
# current=1
# longest=1
# for i in range (1,len(arr)):
#     if arr[i]==arr[i-1]:
#         continue
#     elif arr[i]==arr[i-1]+1:
#                 current+=1
#                 longest=max(current,longest)
#     else:
#         current=1
# print(longest)

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for j in range(len(matrix)):
#     print(matrix[j][0])

# matrix = [
#     [1,0,3],
#     [0,5,6],
#     [7,0,9]
# ]

# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if matrix[i][j]==0:
#             print(i,j)
# matrix = [
#     [1,0,3],
#     [0,5,6],
#     [7,0,9]
# ]
# row=set()
# cols=set()
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if matrix[i][j]==0:
#             row.add(i)
#             cols.add(j)
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         for i in row or j in cols:
#             matrix[i][j]=0
# print(matrix,end="")
# print()\
matrix = [
    [1,0,5],
    [0,5,6],
    [7,0,9]
]
print(len(matrix))
# n=3
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         matrix[j][n-1-i]=matrix[i][j]
# print(matrix)




