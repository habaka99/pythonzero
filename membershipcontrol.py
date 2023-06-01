#admins
admins=["mohsen","Sayed","osama","abdo","omar"]
#welcome message
name=input("please type your name").strip()
if name in admins :
   print(f"welcome back {name}")
   option=input("update or delete")
   if option == "update":  
       newname=input("please enter new name")
       admins[admins.index(name)]=newname
       print(admins)
       print("updated")
   elif option ==  "delete" :
    admins.remove(name)
    print("deleted")
    print(admins)
   else :
    print("you choose no option") 
else:
    status=input("not admin,if you want to be admin y or n").strip()
    if status == "y" or "yes" :
        adminname=input("please enter your name")
        admins.append(adminname)
        print(admins)
    elif status == "n" or "no":
        print("ok")    
