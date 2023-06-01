#search هنا بتعمل ماتش لاول     سترينج بس 
import re
# mysearch=re.search(r"[A-Z]{2}","abdoOOmar")
# print(mysearch)
# print(mysearch.span())
# print(mysearch.string)
# print(mysearch.group())
is_email=re.search(r"[A-z0-9]+@[A-z]+\.(com|net)","abdoomar99@gmail.com")
if is_email:
    print("this email is valid")
else:
    print("this email not valid")
#findall لو في ماتش بترجعلك كل الماتش مش اول ماتش بس وبترجعه في ليست لو ملقتش بترجعلك لييست فاضيه
email_input=input("please enter your mail")
email=re.findall(r"[A-z0-9]+@[A-z]+\.com|net",email_input)
emptyemail=[]
if email != []:
    emptyemail.append(email)
    print("email added")
else:
    print("email is invalid")
for emails in emptyemail:
    print(emails)
