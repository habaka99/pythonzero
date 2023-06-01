user={
    "name":"abdo",
    "age" : 23,
    "country": "egypt",
    "family" : ["ahmed","eslam"],
}
print(user)
print(user["family"])
print(user.get("country"))
print(user.keys())
print(user.values())
print("="*50)
language={
    "one":{
        "name":"python",
        "progress":"80%"
    },
    "two":{
        "name":"css",
        "progress":"70%"
    },
    "three":{
    "name":"html",
    "progress": "50%"
    }
}    
print(language)
print(language["one"])
print(language.get("one"))
print(language["two"]["name"]       )
print(len(language["one"]))
print(50*"=")
frameworkone={
    "name":"nodejs",
    "progress":"50%"
}
frameworktwo={
    "name":"react",
    "progress":"50%"
}
frameworkthree={
    "name":"django",
    "progress":"60%"
}
allframework={
    "one":frameworkone,
    "two":frameworktwo,
    "three":frameworkthree
}
print(allframework)