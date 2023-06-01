#split()
a="I Love Python and php "
print(a.split())
b="I-Love-Python-and-php "
print(b.split("-"))
c="I-Love-Python-and-php "
print(c.split("-",3))
d="I-Love-Python-and-php "
print(d.rsplit("-",3))
#center()
e="abdo"
print(e.center(7,"#"))
#count()
f=" i love python and php and python"
print(f.count("a"))
print(f.count("and",0,26))
#swapcas()
g=" I lOvE pYthon"
print(g.swapcase())
#start with()
h="I lOvE pYthon"
print(h.startswith("l",2,6))
#end with()
m="I lOvE pYthon"
print(m.endswith("n"))