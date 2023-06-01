fname=input('what\'s your first name?')
mname=input('what\'s your middle name?')
lname=input('what\'s your last name?')

fname=fname.strip().capitalize()
mname=mname.strip().capitalize()
lname=lname.strip().capitalize()

print(f"hello {fname} {mname:.1s} {lname}")
