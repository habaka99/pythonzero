# def add(a,b,z=0):
#     return a+b+z
# print(add(1,2))
# print(add(1,2,3))
#poly
# class India:
#     def capital(self):
#         print("the deli is the capital")
#     def labguage(self):
#         print(" indian is language")
# class USA:
#     def capital(self):
#         print("the new work is the capital")
#     def labguage(self):
#         print(" english is language")

# def fun(obj):
#     obj.capital()
#     obj.labguage()
# obj_ind=India()
# obj_usa=USA()
# fun(obj_ind)
# for country in (obj_usa,obj_ind):
#    country.capital()
#    country.labguage()
#poly and inhirtance
# class bird:
#     def intro(self):
#         print("there is many types of birds")
#     def flight(self):
#         print(" flymost of the birds can")    
# class sparrow(bird):
#     def flight(self):
#         print(" sparrow can fly")
# class ostrich(bird):
#     def flight(self):
#         print(" ostrich canot fly")
# bird1=bird()
# bird2= sparrow()
# bird3=ostrich()
# bird1.intro()
# bird1.flight()
# bird2.intro()
# bird2.flight()
# bird3.intro()
# bird3.flight()
class animal:
    def speak():
        raise NotImplementedError("sub class must impl")
        print("wooo")
class dog(animal):
    pass
class cat(animal):
    pass
obj=animal()
obj2=dog()
obj3=cat()
cat.speak()