#map
# def formatname(name):
#     return f"-{name}-"
myname=("ahmed","abdo","sayed")
# ma=map(formatname,myname)
# print(ma)
# for i in map(formatname,myname) :
#     print(i)
for i in map(lambda name : f"-{name}-",myname):
    print(i)
