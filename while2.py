myfr=["ah","sa","mo","to","so","vo"]
#print(len(myfr))
#a=0
#while a< len(myfr):
 #   print(f"#{str(a+1).zfill(2)} {myfr[a]}")
 #   a+=1
#######################
n = int(input().strip())
if n%2 !=0:
        print("Weird")
elif n%2 ==0 and 5>=n>=2:
        print("Not Weird")
elif n%2 ==0 and 6<=n< 20:
        print("Weird")     
elif n%2 ==0 and n>20:
        print("Not Weird")