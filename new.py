# def get_score(**skiils):
#     for x,y in skiils.items() :
#         print(f"{x}>={y}")
# get_score(math="92",science="80",language="97")

# def get_scores(*name,**skiils):
#     if len(skiils)>0:
#         if bool(name):
#             print(f"hello {name} yor score in")
#         for x,y in skiils.items() :
#             print(f"{x}>={y}")
#     else :
#         print("no score to show")
# get_scores(score="90")
score_dict={
    "math":"90",
    "science":"80",
    "lang":"70"
}
def get_score(*name,**score):
    if len(score)>0:
        if bool(name):
          print(f"hello {name}")
        for x,y in score_dict.items():
            print(f"{x}=>{y}")
    else:
        print(f"hello{name} you have no score")
get_score("abdo")


    
