def say_hello(name):
    print(f"hello {name}")
say_hello("ahmed")
def addition(n1,n2):
    if type(n1) != int or type(n2)!=int:
        print("this is string , i need integer") 
    else :   
        print(n1+n2)
addition("100","200")    
def full_name(first,second,last):
    print(f"my name {first.strip().capitalize()}  {second.upper():.1s}  {last.capitalize()}")
full_name(  "ahmed","mohamed","omar")