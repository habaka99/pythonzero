# myskils=["ahmed","abdo","mohsen"]
# # myskillwithenumirate=enumerate(myskils)
# # for c,skill in myskillwithenumirate:
# #     print(f"-{c}- {skill}")
# # print(reversed(myskils))
# # for skil in reversed(myskils):
# #     print((skil))
# mystring="elzero"
# for s  in list(reversed(mystring)):
#     print(list(s))
# print(pow(5,5,5))
# my_range = list(range(15))
# print(sum(my_range,15))#+pow(40,40,40))
# my_all=[1, 2, 3,0]
# def my_any(*num):
#     for i in num:
#         if any(i):
#             print(True)
#         else:
#             print(False)
    
# print(my_any([(), 0, False]))    
# print(my_any([(), 0, False]))
# x=[1,2,3,4,5,0]
# if all(x):
#     print("all element is true")
# else:
#     print("there is one element at least is false")
#print(min(10,15,16))
# def my_min(*num): 
#     for i in num:
#        print(min(str(i)))
# print(my_min(10, 100, -20, -100, 50))
# def my_all(List):
#     k=0
#     for i in List:
#         if bool(i):
#             k+=1
#     if k == len(List):
#         print(True)
#     else:
#         print(False)
# print(my_all([1, 2, 3])) 
#################
# my_list=[(), 0, False]
# def my_any(List):
#     k=0
#     for i in List:
#         if bool(i):
#             k+=1
#     if k >=1:
#         return(True)
#     else:
#         return(False)
# print(my_any(my_list)) # False
# def my_min(List):
#     count=List[0]
#     for i in List:
#         if i < count :
#             count=i
#     return count
# print(my_min([10, 100, -20, -100, 50]))

# def remove_char(chars):
#         return chars[1:-1]
        
    
        
# friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

# #print(map(remove_char,friends_map))
# for s in map(remove_char,friends_map) :
#     print(s)
# def get_name(string):
#     if string.startswith("m"):
#         return string
# friends=["mohamed","samy","mohsenm"]
# name=filter(get_name,friends)
# for i in name:
#     print(i)
# from functools import reduce
# def sumall(num1,num2):
#     return num1*num2
# nums = [2, 4, 6, 2]
# result=reduce(sumall,nums)
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
skiii=reversed(skills)
skillswith=enumerate(skiii,50)
# for  counter,skil in skillswith:
#     if type(skil) == int :
    
#         pass
#     else :
#        print(f"{counter},{skil}")
# def cleaner(name):
#     if type(name[1])==int:
#         pass

# x=filter(cleaner,skillswith)
# for i in x:
#     print(i)
import functools
def sumall(num1,num2):
    return num1+num2
num=[1,2,5,9,20]
result=functools.reduce(sumall,num)
print(result)