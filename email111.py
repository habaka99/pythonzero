thename=input("what is your name?")
theemail=input("what is your email?")

yourname=theemail[:theemail.index("@")].strip()
yourwebsite=theemail[theemail.index("@")+1: ].strip()
print(f"hello your name is {thename} your email is {theemail}")
print(f"your name is {yourname} your website is {yourwebsite}")