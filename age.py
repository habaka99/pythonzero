age=int(input('what\'s yor age?'))
print(f"hello, your age is :{age} years")
months=age*12
weeks=months*4
days=age*365
hours=days*24
minutes=hours*60
second=minutes*60
print(f"you lived {months} months.")
print(f"you lived {weeks} weeks.")
print(f"you lived {days:,} days.")
print(f"you lived {minutes:,} minutes.")
print(f"you lived {second:,} second.")