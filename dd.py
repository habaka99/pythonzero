# def double_letters(par):
#     x=len(par)-1
#     y=0
#     while x>0:
#         if par[y]==par[y+1]:
#             return True
        
#         # elif y==len(par):
#         #     return False
#         y+=1
#         x-=1
#     else:
#         return False
       
# print(double_letters("helo"))
def findsmallest(arr):
    smallest=arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallest_index=i
    return smallest_index
def secection_sort(arr):
    newarr=[]
    for i in range(len(arr)):
        smallest=findsmallest(arr)
        newarr.append(arr.pop(smallest))
    return newarr
print(secection_sort([5,6,2,10]))