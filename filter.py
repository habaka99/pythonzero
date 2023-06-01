#filter
def checknum(num):
    if num ==   0:
        return True
mynum=(0,0,1,20,30,40,10,5,90,0)
ma=filter(checknum,mynum)
# print(ma)
# for i in filter(checknum,mynum) :
#     print(i)
for i in filter(lambda num : True if num == 0 else None ,mynum  ):
    print(i)
# def checkname(name):
#    return name.startswith("o")
# myname=("osama","omar","omer")
# nu=filter(checkname,myname)
# # print(ma)
# for i in filter(checkname,myname) :
#     print(i)