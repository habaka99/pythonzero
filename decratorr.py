# def mydecrator(fun):
#     def tazeenO(num1,num2):
#         print("before decoration")
#         fun(num1,num2)
#         print("after decoration")
#     return tazeenO
# @mydecrator
# def sayhello(n1,n2):
#     print(n1+n2)
# # mydeco=mydecrator(sayhello)
# # mydeco()
# sayhello(10,20)
# def shout(text):
#     return text.upper()
 
# shout('Hello')
# def create_adder(x):
#     def adder(y):
#         return x+y
 
#     return adder
 
# print(create_adder(15))
# add_15 = create_adder(15)

# print(add_15(10))
# def hello_decorator(func):
#     def inner1(*args, **kwargs):
         
#         print("before Execution")
         
#         # getting the returned value
#         returned_value = func(*args, **kwargs)
#         print("after Execution")
         
#         # returning the value to the original frame
#         return returned_value
         
#     return inner1
 
 
# # adding decorator to the function
# @hello_decorator
# def sum_two_numbers(a, b):
#     print("Inside the function")
#     return a + b
 
# a, b = 1, 2
 
# # getting the value through return of the function
# print( sum_two_numbers(a, b))
# import math
# print(dir(math))
import time
def speedtest(fun):
    def wrapp():
        start=time.time()
        fun()
        end=time.time()
        print(f"running time is{end - start}")
    return wrapp
@speedtest
def bigloop():
    for num in range(1,20000):
        print(num)
bigloop()