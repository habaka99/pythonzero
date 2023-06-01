# def printresult(String) : 
#     for i in String: 
#         if i == "e": 
#             return i 
# string="geeksforgeek"
# ans=0
# for i in printresult(string):
#     ans+=1
# print(f"The number of 'e' in word is :{ans} ")

# def fib(limit):
#     a,b=1,2
#     while a < limit:

#         return a  
#         a, b = b, a + b
# print(fib(5))
# b = "Hello, World!"
# print(b[::-1])
def reverse_string(my_string):
  # Your Code Here
  
  for i in reversed(my_string):
    yield i
# Reverse The String
for c in reverse_string("Elzero"):
  print(c)