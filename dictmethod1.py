#clear
user={
    "name":"osama"
}
print(user)
user.clear()
print(user)
#update
member={
    "name":"osama"
}
print(member)
member["age"]=36
print(member)
member.update({"country":"egypt"})
print(member)
#copy
main={
    "name":"osama"
}
b=main.copy()
print(main)
print(b)
main["age"]=36
print(main)
print(b)
#setdeafult
user={
    "name":"osama"
}
print(user.setdefault("name","abdo"))
print(user)
user.setdefault("age",35)
print(user)
#opoitem()
member={
    "name":"osama",
    "skill":"fight"
}
print(member.popitem())
#items
view={
    "name":"osama",
    "skill":"xbox"
}
allitems=view.items()
print(view)
print(allitems)
#fromkeys
a={"keyone","keytwo","keythree"}
b={"x"}
print(dict.fromkeys(a,b))