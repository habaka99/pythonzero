name="osama"
print("a" in name)
print("s" in name)
print("S" not in name)

print("="*50)
friends=["ahmed","mohamed","sayed"]
print("osama" in friends)
print("ahmed" in friends)
print("ahmed"not in friends)

print("="*50)
mycountry=input('what\'s your country').strip().capitalize()
countriesone=("Egypt","Ksa","Kwait","Qatar")
discountone=80
countriestwo=("Italy","Sudan")
discounttwo=30
if mycountry in countriesone :
    print(f"you have discount equal= {discountone}")
elif mycountry in countriestwo :
    print(f"you have discount equal={discounttwo}")
else :
   print(f"your country  {mycountry} dont have dsicount ")