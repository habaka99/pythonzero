#replace (old ,new,count)
a= "hello one two one one"
print(a.replace("one","three",1))
print(a.replace("one","three",2))
print(a.replace("one","three",3))
#join(iterable تقدر تعمل عليه لوب)
b=  ["abdo","mohame","omar"]
print("-".join(b))
name="abdo"
age=23
rank=10
print("my name is %s and my age %d and my rank%f "% (name,age,rank))
print("my rank %.3f " % (rank))

#%placeholder %s string , %d digit ,%f float 
#control floating number
#truncate string 
mystring="i--love-body-and-mody"
print("my massage %.6s "%(mystring  ))
print(mystring)