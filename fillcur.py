myfiles = open(r"C:\Users\abdo1\python\abdo.txt" , "r")
# print(myfiles.tell())
# myfiles.truncate(10)
myfiles.seek(12)
print(myfiles.read())