num=int(input("please enter the numver"))
sum=num
if num <= 0 :
    print("the number less than 0")
else:
    #sum=0
    while num>1:
       num-=1
       if num == 6:
        continue
       print(num)
      # sum+=1

print(f"{sum-2}the number succefly pritnt")
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
a=0
while a<len(friends):
    if friends[a].istitle():
        print(friends[a])
    a+=1        
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
while skills:
    print(skills.pop(-1))
my_friends=[]
maxfriend=4
while maxfriend>0:
        frinname=input("enter your friend name")
        maxfriend-=1
        if frinname.isupper():
          print("name is not valid")
        elif frinname.islower():
          frinname.capitalize()
          my_friends.append(frinname)        
          print(f"Friend {frinname} Added => 1st Letter Become Capital")
        else :
            my_friends.append(frinname)        
            print(f"Friend {frinname} Added")
        print(f"name lift in list is {maxfriend}")if maxfriend>0 else print("all")


