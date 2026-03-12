# arr=[3,4,6,7,9,12,16,17]
# target=9
# low=0
# high = len(arr)-1
# while low<=high:
#     mid=(low+high)//2
#     if arr[mid]==target:
#         print(mid)
#         break
#     elif target>arr[mid]:
#         low=mid+1
#     elif target<arr[mid]:
#         high = mid-1
#     else:
#         print("not found ")
# arr=[1,2,3,3,5,8,8,10,10,11]
# x=8
# low=0
# high=len(arr)-1
# ans=len(arr)
# while(low<=high):
#     mid=(low+high)//2
    
#     if arr[mid]>=x:
#         ans=mid
#         high=mid-1
#     else:
#         low=mid+1
# print(ans)
        

# first=-1
# last=-1
# x=8
# for i in range(len(arr)):
#     if arr[i]==x:
#         first=i
#         last=i
#         break
# for j in range(first,len(arr)):
#     if arr[j]==x:
#         last=j
# print(first,last)
# x=8
# low = 0
# high = len(arr) - 1
# first = -1
# last = -1
# while low<=high:
#     mid=(low+high)//2
# if arr[mid]==x:
#     ans=mid


# arr=[2,4,6,8,10]
# x=7
# floor=-1
# ceil=-1
# low=0
# high=len(arr)-1
# while low<=high:
#     mid=(low+high)//2
#     if arr[mid]<=x:
#         floor=arr[mid]
#         low=mid+1
#     else:
#         ceil=arr[mid]
#         high=mid-1
# print(floor,ceil)

# arr=[2,4,6,8,10]
# x=7
# floor=-1
# ceil=-1
# low=0
# high=len(arr)-1
# while low<=high:
#     mid=low+high//2
#     if arr[mid]<=x:
#         floor=mid
#         low=mid+1
#     else:
#         ceil=mid
#         high=mid-1
# print(floor,ceil)

# arr = [2,4,6,8,8,8,11,13]
# x = 8
# first=-1
# last=-1
# low=0
# high=len(arr)-1
# while low<=high:
#     mid=(low+high)//2
#     if arr[mid]==x:
#         first=mid
#         high=mid-1
#     elif arr[mid]<x:
#         low=mid+1
#     else:
#         high=mid-1
# print(first,last)


#search in rotated sorted array
# target=4
# arr=[4,5,6,7,0,1,2]
# low=0
# high=len(arr)-1
# while low<=high:
#     mid=(low+high)//2
#     if arr[mid] == target:
#         break
    
#     elif arr[low]<=arr[mid]:
#         if arr[low]<=target<arr[mid]:
#             high=mid-1
#         else:
#             low=mid+1
    
#     else:
#         if arr[mid]<target<=arr[high]:
#             low=mid+1
#         else:
#             high=mid-1
# print(mid)

# #binary search
# ans=1
# arr=[1,2,3,4,5,6,7,8,9,16]
# low=0
# high=len(arr)-1
# x=16
# while(low<=high):
#     mid=(low+high)//2
#     if arr[mid]*arr[mid]==x:
#         ans=arr[mid]
#         break
    
#     elif arr[mid]*arr[mid]<x:
#         ans=mid
#         low=mid+1
#     else:
#         high=mid-1
# print(ans)


#finding nth root of an integer
# arr=[1,2,3,4,5,6,7]
# ans=0
# low=0
# high=len(arr)-1
# n=3
# m=16
# while(low<=high):
    
#     mid=(low+high)//2
#     if arr[mid]**n==m:
#         ans=arr[mid]
#         break
#     elif arr[mid]**n<m:
#         ans=arr[mid]
#         low=mid+1
#     else:
#         high=mid-1
# print(ans)
        

#find smallest divisor give a threshold 
import math
sum=0
arr=[1,2,5,9]
threshold=6
low=min(arr)
high=max(arr)
while low<=high:
    mid=(low+high)//2
    sum=0
    for i in arr:
        sum+=math.ceil(i/mid)
    if sum<=threshold:
        ans=mid
        high=mid-1
    else:
        low=mid+1
print(ans)
        