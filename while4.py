tries=4
while tries>0 :
    passward=input("plese enter your pssaward")
    mainpassward="Aabdoomar"
    if passward != mainpassward:
        tries-=1
        print(f"your passard incorrect,you have {'last chance'if tries==1 else tries}tries")
else:
    print("you make pass write pass")
    