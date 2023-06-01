# def decro(fun):
#     def tecro():
#         print("Sugar Added From Decorators")
#         fun()
#         print("#"*50)
#     return tecro
# @decro
# def make_tea():
#   print("Tea Created")
# @decro
# def make_coffe():
#   print("Coffe Created")
# make_tea()
# make_coffe()
listp=["ahmed","r7ma","dalia"]
name=input("whatistourname?").strip().capitalize()
if name in listp:
    print("you are admin")
else:
    print("you are not admin")