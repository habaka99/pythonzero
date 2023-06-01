# stocks = ['reliance', 'infosys', 'tcs']
# prices = [2175, 1127, 2750]
 
# new_dict = {stocks: prices for stocks,
#             prices in zip(stocks, prices)}
# print(new_dict)
list1=[1,2,3,4,5,6]
tuble1=("abdo","omar","mohsen")
dict1={"python":"70%",
       "css":"80%",
       "html":"60%"
}
zipo=zip(list1,tuble1)
# for c,(i,x,z) in enumerate(zip(list1,tuble1,dict1),5):  #خلي بالك كان لازم تحط الitem بتاعت zip في اقواس
#     print(c,i,"your name",x,"and your skills",z,dict1[z])
print(set(zipo))