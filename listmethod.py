mybrother=["ahmed","eslam","abdo"]
print(mybrother)
mybrother.append("mohamed")
print(mybrother)
myfamily=["mama","baba",100]
mybrother.append(myfamily)
print(mybrother)
print(mybrother[4])
print(mybrother[4][0])
#extend 
a=["abdo","mohamed","omar"]
b=["student","faculty","pharmacy"]
c=["soldger","abdo","mohamed"]
a.extend(b)
a.extend(c)
print(a)
#remove
a.remove("abdo")
print(a)
#sort
v=[1,6,0,-22,100,55]
e=["a","z","e"]
v.sort()#sort(reversa=false)
e.sort(reverse=False)
print(v)
print(e)
v.sort(reverse=True)
e.sort(reverse=True)
print(v)
print(e)
g=[1,2,"body"]
print(g.pop(2))
print(g)