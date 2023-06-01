class member:
    #class atribute
    not_allowed_name=["ballo","shit","hell"]
    user_num=0
    @classmethod
    def show_user_count(cls):
        print( f"{member.user_num}")
    @staticmethod
    def say_hello():
        print(f"hello ")
    def __init__(self,first_name,second_name,last_name,gender) :
        self.fname=first_name
        self.mname=second_name
        self.lname=last_name
        self.gend=gender
        
        member.user_num+=1

    def full_name(self):
        if self.fname in member.not_allowed_name:
            raise ValueError ("name is not allowed")
        return f"{self.fname} {self.mname} {self.lname}"
    def with_title(self):
        if self.gend == "male":

          return f"hello MR {self.fname}"
        elif self.gend  == "female":
            return f"hello MISS {self.fname}"
    def full_info(self):
        return f"{self.with_title()},your full name {self.full_name()}"
    def delete_user(self):
        member.user_num-=1
        return f"user{meber_one.fname} is deleted"

print(member.user_num) 
meber_one=member("ahmed","elsayed","abdo","male")
meber_two=member("ezz","eyt","mohamed","male")
meber_three=member("Mona","elsyed","Arafa","female")
meber_four=member("shit","balo","Arafa","female")
print(member.user_num)   
print(meber_one.delete_user())
print(member.user_num) 

print(meber_three.full_info())
# print(meber_three.with_title())

# print(meber_two.fname,meber_two.mname,meber_two.lname)
# print(meber_three.full_name())
member.show_user_count()
member.say_hello()