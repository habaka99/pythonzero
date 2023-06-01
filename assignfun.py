def calculate(n1,n2,operator="add"):
    operator=operator.lower()
    if operator == "add"or operator == "a":
        print(n1+n2)
    elif operator == "substract"or  operator=="s":
        print(n1-n2)
    elif operator == "multiply" or operator=="m":
        print(n1*n2)
    else :
        print("error, no operator")    
calculate(1,2,"s")
calculate(1,2,"S")
calculate(1,2,"M")
calculate(1,2,"m")

def addition(*num):
    code=0
    for nu in num :
        if nu ==10:
            continue 
        elif nu ==5:
            code-=5  
        code+=nu    
    print(code)    
addition(10,20,30,10,15)


def details(name,*skills):
       if len(skills)>0:
         print(f"hello {name} your skill is")
       for skill in skills:
          print(f"-{skills}")
       else :
           print(f"hello {name}you have no skill")   

details("abdo")
 
def say_hello (name,age,country="uknown"):
    print(f"Hello {name} Your Age Is {age} And You Live In {country}")
say_hello("abdo",25)