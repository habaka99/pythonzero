myfavouriteweb=[]
maximumweb=5
while maximumweb >0 :
    web=input("your favourite web without https\:").strip().capitalize()
    myfavouriteweb.append(f"https\:{web}")
    maximumweb-=1
    print(myfavouriteweb)
else:
    print("bookmark are full,you cant add more")  

if len(myfavouriteweb)>0 :
    myfavouriteweb.sort()
    index=0
    while index <len(myfavouriteweb):
        print(myfavouriteweb[index])
        index+=1