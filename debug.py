""" this function
 for say hello
 to create"""

myFriends = ["Ahmed", "Osama", "Sayed"]

def say_hello(some_people) -> list:
    """ this function for say hello"""
    for some_one in some_people:
        print(f"Hello {some_one}")
say_hello(myFriends)
