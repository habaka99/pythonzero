#split لو انا عايز اقص جملة من عند منطقة معينة والمنطقة دي هتكوت الناتش الي انا هختاري
import re
# one="hello abdo how are you"
# search_one=re.split(r"\s",one)
# print(search_one)
#max split mean specifya part to cut from
# one="hello abdo how are you"
# search_one=re.split(r"(\s)",one,1)
# print(search_one)
#loop on the spliting list
# two="how-are_you_and-your-a-family-an-brater"
# searchtwo=re.split(r"-|_",two)
# print(searchtwo)
# for counter,word in enumerate(searchtwo,1):
#     if len(word)<3:
#         continue
#     print(f"th counter of word>={counter} and the word {word.upper()}")
#sub ([pattern,replace,string,count])
# one="hello abdo how are you"
# search_one=re.sub(r"\s","-",one,2)
# print(search_one)