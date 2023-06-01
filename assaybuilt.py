values = (0, 1, 2)

if any(values):

  my_var = 0
print("all element is true")
#هناanyبتكون عايزه واحد بس من العناصر يكون موجود 
my_list = [True, 1,  1, ["A", "B"], 10.5105, my_var]

if all(my_list[:4]) and all(my_list[:6]) and all(my_list[:]):

  print("Good")

else:

  print("Bad")
for i in range(1,100):
   if round(sum(list(range(i))) / i) == 10:
       print(i)