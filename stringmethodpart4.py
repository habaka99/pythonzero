#index
a="i love python"
print(a.index("y",0,9))
#find
b="i love python"
print(b.find("y",0,8))
#rjust,ljust
c="abdo"
print(c.rjust(10,"#"))
print(c.ljust(10,"#"))
#spilitline
d="first line\nsecondline\nthirdline"
print(d.splitlines())
e="""first line
secondline
thirdline"""
print(e.splitlines())
#expandtabs
f="I\tlove\tpython\tand\tme"
print(f.expandtabs(3))
one="I Love Pyhon 3G"
print(one.istitle())
two=" "
print(two.isspace())
#identifier
six="abdoomar"
seven="abdo---omar"
eight="abdoomar9999"
print(six.isidentifier())
print(seven.isidentifier())
print(eight.isidentifier())
x="aaaannnnnn"
t="jfvbjv99"
print(x.isalpha())
print(t.isalnum())