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
        }
}
for main_key,main_value in peoples.items() :
    print(f"{main_key}")
    for child_key,child_value in main_value.items():
        print(f"{child_key}>={child_value}")

   