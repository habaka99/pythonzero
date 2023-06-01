 # class member:
#     def __init__(self,name):
#         self.name=name
# one=member("ahmed")
# print(one.name)
# one=member("sayed")
# print(one.name)
# class member:
#     def __init__(self,name):
#         self._name=name
# one=member("ahmed")
# print(one._name)
# one=member("sayed")
# print(one._name)

class member:
    def __init__(self,name):
        self.__name=name
    def say_hello(self):
        print (f"this name is {self.__name}")
    def get_name(self):
        return self.__name
    def change_name(self,name_new):
        self.__name=name_new
one=member("ahmed")
# print(one.__name)
# one=member("sayed")
# print(one.__name)
# one.say_hello()
# print(one.get_name())
# one.change_name("mohsen")
# one.say_hello()
class member:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def say_hello(self):
        return (f"this name is {self.name}")
    @property
    def age_in_days(self):
        return self.age*365
one=member("ahmed",50)
print(one.say_hello())
print(one.age_in_days)


