# def sum(lis):#[1,2,3,4]
#     total=0
#     for i in lis:
#         total+=i
#     return total
# # print(sum([1,2,3,4]))
# def count_number(list1):
#     count=0
#     for i in list1:
#         count+=1
#     return count
# print(count_number([1,2,3,4]))
# def sum(lis):
#     if lis == []:
#         return 0
#     return lis[0]+sum(lis[1:])
# print(sum([1,2,3,4]))
# def count_number(lis):
#     if lis==[]:
#         return 0
#     return 1 + count_number(lis[1:])
# print(count_number([1,2,3,4]))
# def max(lis):
#         if len(lis)==2:
#             return lis[0]if lis[0]>lis[1]else lis[1]
#         else:
#             sub_max=max(lis[1:])
#         return lis[0] if lis[0]>sub_max else sub_max
# print(max([4,5,1,2]))
# # items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


# def find_max(items):
#     if len(items) == 1:
#         return items[0]

#     op1 = items[0]
#     # print(op1)
#     op2 = find_max(items[1:])
#     # print(op1, op2)

#     if op1 > op2:
#         return op1
#     else:
#         return op2


# print(find_max(items))
# def recursive_max(arr):
#     if len(arr) == 0:
#         return None
#     elif len(arr) == 1:
#         return arr[0]
#     else:
#         maxItem = recursive_max(arr[1:])
#         return maxItem if maxItem > arr[0] else arr[0]
# print(recursive_max([1,2,5,4]))
def min_num(m):
    if len(m)==2:
        return m[0] if m[0]<m[1] else m[1]
    else:
        sub_min=min_num(m[1:])
        return m[0] if m[0]<sub_min else sub_min
print(min_num([1,2,5,4]))
