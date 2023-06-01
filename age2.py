#note
print(80*"#")
print("you can write first litter or full name".center(80,"#"))
print(80*"#")
#collect age
age=input("please write age").strip()
#collect time unit
unit=input("please choose your time unit:months,weeks,days")
#get time unit
months=int(age)*12
weeks=months*4
days=int(age)*365
if unit == "months" or unit == "m":
    print("you choose the unit months.")
    print(f"you lived for {months:,}months.")
elif unit == "weeks" or unit=="w":
    print("you choose the unit time ")
    print(f"you lived for {weeks: ,} weeks.")
elif unit == "days" or unit=="d":
    print("you choose the unit time ")
    print(f"you lived for {days:,} days.")    
