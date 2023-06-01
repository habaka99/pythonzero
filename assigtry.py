# Num = (input("Add Your Number "))
# if len(Num)>1:
#     raise IndexError("Only One Character Allowed")
# elif len(Num)==1:
#     print(f"the number {Num}")
# elif int(Num) == 0:
#     raise ValueError("Number Must Be Larger Than 0")
# elif Num.isalpha():
#     print("Only Numbers Allowed")
try:
    LETTER = input("Add Letter From A to Z")
    if len(LETTER)  != 1:
        raise ValueError
    # if LETTER.isupper():
    #     print(f"You Typed {LETTER}")
except ValueError:
    print("frfr")

