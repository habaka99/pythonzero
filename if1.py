uname="osama"
country=input("what is yur country")
isstudent=input("are you student?")
cname="python course"
price=100
if country == "egypt" or   country == "ksa" or  country == "bahrin" and  isstudent== "yes":
      print(f"hello {uname} the course is {cname} and becouser you are from {country} and you are student the price:{price-90}")
else :
        print(f"hello {uname} the course is {cname} and the price:{price-20}")
