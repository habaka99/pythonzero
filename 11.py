# # Our counter function
# def counter():
#   c = 0 # Local counter variable
   
#   # This function manipulate the
#   # local c variable, when called
#   def count():
#     nonlocal c
#     c += 1
#     return c
   
#   # Return the count() function to manipulate
#   # the local c variable on every call
#   return count
# my_counter = counter()

# print(my_counter())
# def function(string):
#     string2 = '|'.join([i for i in string])
#     [print(string2, end=' ') for i in range(4)]
# function('brian')
def countdown(i):
  print(i)
  countdown(i-1)
countdown(5)