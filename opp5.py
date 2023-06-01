# from abc import ABCMeta,abstractproperty
# class a(metaclass=ABCMeta):
#     # @abstractproperty
#     def has_opp(self):
#         return "yes"
# class b(a):
#    pass
# class c(a):
#     def has_opp(self):
#         return "no"
# one=b   ()
# print(one.has_opp())
#assign
# class Game:
#   # Write Class Content
#   def __init__(self,name,developer,year,price):
#      self.name=name
#      self.developer=developer
#      self.year=year
#      self.price=price
#     #  self.price=price
#   def price_in_pounds(self):
#      return f"{self.price*16} egyption pound"
     

# game_one = Game("Ys", "Falcom", 2010, 50)

# print(f"Game Name Is \"{game_one.name}\", ", end="")
# print(f"Developer Is \"{game_one.developer}\", ", end="")
# print(f"Release Date Is \"{game_one.year}\", ", end="")
# print(f"Price In Egypt Is {game_one.price_in_pounds()}", end="")
# class User:
#   # Write Class Content
#   def __init__(self,n1,n2,age,gender):
#     self.n1=n1
#     self.n2=n2
#     self.age=age
#     self.gender=gender
#   def full_details(self):
#         if self.gender=="Male":
#           return f"hello mr {self.n1} {self.n2:.1s}. {self.age-40} yaers to reach 40"
#         elif self.gender=="Female":
#           return f"hello miss {self.n1} {self.n2:.1s}. {self.age-40} yaers to reach 40"


# user_one = User("Osama", "Mohamed", 38, "Male")
# user_two = User("Eman", "Omar", 25, "Female")

# print(user_one.full_details()) # Hello Mr Osama M. [02] Years To Reach 40
# print(user_two.full_details()) # Hello Mrs Eman O. [15] Years To Reach 40
# class Message:
#    def __inti__(self):
#       pass
#    @staticmethod
#    def print_message():
#       return "Hello From Class Message"

# print(Message.print_message())
# class Games:
#   # Write Class Content

# my_game = Games("Shadow Of Mordor")
# my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
# my_games_count = Games(80)

# my_game.show_games()


# my_games_names.show_games()

# my_games_count.show_games()
class Members:

  def __init__(self, n, p):

    self.name = n

    self.permission = p

  def show_info(self):

    return f"Your Name Is {self.name} And You Are {self.permission}"
class Admins(Members):
    def __init__(self, n, p):
       super().__init__(n, p)
class Moderators(Admins):
    def __init__(self, n, p):
       super().__init__(n , p)
member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")
print(member_one.show_info())
print(member_two.show_info())
###################
class A:

  def __init__(self, one):

    self.one = one

class B:

  def __init__(self, two):

    self.two = two

class C(A):

  def __init__(self, three):

    self.three = three
class Text(C,B):
     def __init__(self):
         super(C,B).__init__()
     def show_name(self):
        return f"The Name is {self.one}{self.two}{self.three}"
the_name = Text("El", "ze", "ro")
# print(the_name)
print(the_name.show_name())
import os