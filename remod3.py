import re
one="https://www.Elzero.org:8080/category.php?article=105?name=how-to-do"
search=re.search(r"(https?)://(www.)?([a-z]+)\.(\w+):?(\d+)?/(.+)",one,re.IGNORECASE)
# print(search.group())
print(search.groups())
for searchh in search.groups():
    print(searchh)