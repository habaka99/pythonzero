myskiils=("css","js","html")
myskiils={
    "go":"80%",
    "pyhton":"70%"
}



def show_skill(name, *skills,**skiils):
    print(f"hey {name} your skill without progress")
    for skill in skills:
        print(f"-{skill}")
    print(f"hey {name} your skill  progress")
    for skiil in skiils:
        print(f"-{skiil}")    

show_skill("abdo",*myskiils,**myskiils)
#x=2#glopal
def one():
    global x
    x=1 #local
    print(f"print variable from global scope{x}")
def two():
    x=10
    print(f"print variable from global scope{x}")

one()
print(f"print variable from global scope{x}")
two()

