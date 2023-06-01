class baseone:
     def __init__(self):
          print("base one")
     def fun_one(self):
          print("one")
class basetwo:
     def __init__(self):
          print("bas two")
class derived(baseone,basetwo):
     pass
arg=derived()
print(arg.fun_one)
#resuliotion order 
print(derived.mro())










