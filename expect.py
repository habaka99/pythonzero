# x=-1
# if x<0:
#     raise Exception (f"number is less than 0") 
# else:
#     print("ok number is valid")
y=10
if type(y) != int:
    raise Exception("string not allowed")
else:
    print("number allowed")