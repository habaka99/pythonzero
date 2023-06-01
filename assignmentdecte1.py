a=[1,5,4,3,3,2,1]
a.sort()
print(a)
unique_list=[1,2,3,4,5]
print(unique_list)
print(type(unique_list))
unique_list.pop(-1)
print(unique_list)
#
nums = {1, 2, 3}
letters = {"A", "B", "C"}
print(nums | letters)
print(nums.union(letters))
nums.update(letters)
print(nums)
#
my_set = {1, 2, 3}
my_set.clear()
print(my_set)
a={"A","B"}
my_set.update(a)
print(my_set)
my_set.discard("c")
print(my_set)
letters = {"A", "B", "C"}
#
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issuperset(set_two))
#
dict1={
    "Name":"HTML",
    "PROGRESS": "90%"
}
dict2={
    "Name":"PYTHON",
    "PROGRESS": "30%"
}
dict3={
    "Name":"CSS",
    "PROGRESS":"80%"
}
DECT4={
    "ONE":dict1,
    "TWO":dict2,
    "THREE":dict3
}
print(DECT4)
print(DECT4["ONE"])
#
html = 80
css = 60
javascript = 70
print(html>50 and css>50 and javascript>50)
#
num_one = 10
num_two = 20
num = 20
print(num>num_two or num >num_one)
print(num>num_two and num >num_one)
#
um_one = 10
num_two = 20
result=um_one + num_two
print(result)
print(result**3)
print(27000%26000)
a=(1000/5)
print(type(str(a)))
