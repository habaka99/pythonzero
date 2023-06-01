import timeit
# print(timeit.timeit("'Elzero' * 1000"))
# name="abdo"
# print(name)
import random
# print(random.randint(5,15))
# print(timeit.repeat(stmt="name ='abdo' ; name *1000",repeat=2))
print(timeit.repeat(stmt="random.randint(5,15)",setup="import random",repeat=4))