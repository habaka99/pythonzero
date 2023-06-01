#1
#int
print(1)
#float
print(5.20)
#complex
print(5+6J)
#2
i=1+6J
print("imignary part is:{}".format(i.real))
print("imignary part is:{}".format(i.imag))
#3
num=10
print(float(num))
#4
num1=159.650
print(int(159.650))
print(type(int(159.650)))
#5
print(100-115)
print(50*30)
print(21%4)
print(110 / 11)
print(97//20)
#6
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0])
#print(friends.pop(0))
print(friends[-1])
#print(friends.pop(-1))
print(friends[0:5:2])
print(friends[1:5:2])
#7
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[2:5])
print(friends[-2:])
#8
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends[3:]=["elzero","elzero"]
print(friends)
#9
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends.insert(0,"nasser")
print(friends)
friends.insert(-1,"abdo")
print(friends)
#9
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
friends.extend(employees)
friends.extend(school)
print(friends)
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends))
#print(count(friends))
#11
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[4][0])
print(technologies[4][2])