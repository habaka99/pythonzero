#num1=20
num2=40
operation="+"
age1=17
print("app is good for you"if age1>16 else "app is not good for you")
print("#"*80)
age2=int(input("whats your age "))
months=age2*12
weeks=months*4
days=weeks*365
hours=days*24
minutes=hours*60
second=minutes*60
print(f"your age is {months} months.")
print(f"your age is {weeks} weeks.")
print(f"your age  is {days:,} days.")
print(f"your age is {minutes:,} minutes.")
print(f"your age is {second:,} second.")
if 10<age2<100 :
        print("ok")
else:
    print("your age is out of range")    
###############3
country = str(input("Input Your Country")).strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30
if country == countries :
    print(f"yur country {country} Eligible For Discount And The Price After Discount Is ")
else :
    print("ok")    
