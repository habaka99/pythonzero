#list not array 
mylist=["one","two","three",100]
print(mylist)
#indexing
print(mylist[0])
print(mylist[-1])
print(mylist[-3])
#slicing
print(mylist[0:2])
print(mylist[0:])
print(mylist[:4])
#edit
mylist[0]="three"
print(mylist)
mylist[0:3]=["a","b","c"]
print(mylist)
mylist[0:]=["body","dody"]
print(mylist)