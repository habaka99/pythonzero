myfile=open(r"C:\Users\abdo1\python\abdo.txt" , "r")
# print(myfile)
# print(myfile.name)
# print(myfile.mode)
# print(myfile.encoding)

# print(myfile.read())
# print(myfile.readline())
# print(myfile.readline(8))
# print(myfile.readline())
# print(myfile.readlines())
# print(myfile.readlines(20))
for line in myfile:
    print(line)
    if line.startswith("07"):
        break
myfile.close