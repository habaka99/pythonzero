# from PIL import Image
# myimage=Image.open(r"C:\Users\abdo1\myfiles\rainbow.jpg")
# #showimage
# myimage.show()
# # myimage.show()
# # import sys 
# # print(sys.path)
# #cropimage
# mybox=(200,200,500,500)
# mynewimage=myimage.crop(mybox)
# #show crobedimage
# mynewimage.show()
# #converted image
# myconverted=myimage.convert("L")
# myconverted.show()
def say_hello(name):
    """
    the function do how areyou
    and your mother 
    """
    print(f"hello {name}")
print(say_hello.__doc__)
help(say_hello)