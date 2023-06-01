def say_hello(*peoples):
    for people in peoples:
        print(f"hello {people}")
say_hello("abdo","body","dody","toty")        
def show_details(name,*skills):
    for skill in skills:
        print(f"hello {name} your skill is{skill}")
show_details("sayed","html","css","python")