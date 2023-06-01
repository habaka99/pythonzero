#range
#for range in range(1,50):
  #  print(range)
myskill={
    "python": "90%",
    "html":"20%",
    "css":"60%",
    "mysql":"90"
}
#print(myskill)
print(myskill["python"])
print(myskill.get("python"))
for skill in myskill:
    print(f"my progress in lang {skill} is:{myskill.get(skill)}")