my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums.sort(reverse=True)
calc=0
for num in my_nums:
    if num % 5 == 0 :
      calc+=1
      print(f"{calc} => {num}")      
print("all ")
for i in range(1,21):
        #print(str(i).zfill(2    )) 
        if i in [6,5,9]:
            continue
        if i<10:
            print(f"0{i}")
        else:
            print(i)    
my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}
ranks={
    "A":"100",
    "B":"80",
    "C":"40"
}
code=0
for keys,values in my_ranks.items():
    print(f"My Rank in {keys} is {values} And This EQUAL {ranks[values]} ")
    code+=int(ranks[values])
else:
    print(f"total point is {code}")   
students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
} 
ranks={
    "A":"100",
    "B":"80",
    "C":"40",
    "D":"20"
}
code1=0
for name in students:
    print("="*10)
    print(f"students name =>{name}")
        print("="*10)

    for main_keys,main_values in students[name].items():
        print(f"{main_keys}=>{ranks[main_values]}")
        code1+=int(ranks[main_values])
    print(f"total points for{name}is{code1}")