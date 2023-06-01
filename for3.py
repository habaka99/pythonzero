#peoples=["ahmed","sayed","mohsen"]
#skills=["css","html","python"]
#for name in peoples:
#    print(f"name is{name}")
#    for skill in skills:
#        print(f"-{skill}")
peoples={
    "ahmed":{
        "css":"90%",
        "html":"80",
        "python":"50"
    },
    "sayed":{       
        "css":"90%",
        "html":"80",
        "python":"50"
    },
    "body":{
        "css":"90%",
        "html":"80",
        "python":"50"
    }
}
for name in peoples:
    print(f"name is {name}")
    for skill in peoples[name]:
        print(f"skill is {skill} and progress :{peoples[name][skill]}")