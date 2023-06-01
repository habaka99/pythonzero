# my_list = ["E", "Z", "R", 1, 2, 3]
# my_tuple = ("L", "E", "O")
# my_data = []

# for data in zip(my_list, my_tuple):
#   # Write Your Code Here
#   my_data.extend(data)
#   finalresult=my_data.pop[0]
# #   finalresult=("".join(my_data))
# print(finalresult)
# # print(my_data)
# # print(i)
# my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
# my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
# my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
# my_data = []

# for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
#   # Write Your Code Here
#   my_data.append(item1)
#   if len(my_data) == len("elzero"):
#     print(my_data)
#     final_string="".join(my_data)

# print(final_string)
""" this function for say hello"""
myFriends = ["Ahmed", "Osama", "Sayed"]
def say_Hello(Some_Peoples) -> list:
    """ this function for say hello"""
    for Some_one in Some_Peoples:
        print(f"Hello {Some_one}")
say_Hello(myFriends)
# from PIL import Image
# myimage=Image.open(r"C:\Users\abdo1\myfiles\elzero-pillow.png")
# # myimage.show()
# lcroped=(800,0,1200,400)
# lcropedimg=myimage.crop(lcroped)
# lcropedimg.show()
# # newimage=lcropedimg.convert("L")
# # newimage.show()
# # newimage.save("limaeg.png")