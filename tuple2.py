mytuple1=("abdo",)
mytuple2="abdo",
print(type(mytuple1))
print(type(mytuple2))
print(len(mytuple1))
#cocca
a=(1,2,3)
b=(3,4,5)
c=(a+b)
print(c)
#repeat*
mystring="osama"
mylist=["a","b"]
mytuple=(1,2)
print(mystring*6)
print(mylist*6)
print(mytuple*6)
#count
d=(5,5,5,69,0,6,0)
print(d.count(5))
print(d.count(0))
#index
m=(1,2,2,3,3,45,6)
print(m.index(6))
print("this position of index:{:d}".format(m.index(6)))
print(f"this position of index:{m.index(6)}")
#detruct
a=("a","b","C","e")
x,y,z,_=a
print(x)
print(y)
print(z)