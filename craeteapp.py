#import sqlite
import sqlite3
#connect data 
db=sqlite3.connect("app.db")
#curour
cr=db.cursor()
def commit_and_close():
    db.commit()
    db.close()
    print("db connection is closed")
#user_id
uid=1
input_masseage="""
what do you want to do ?
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete skill
"u" => Update Skill Progress 
"q" => Quit The App
choose option:
"""
user_input=input(input_masseage).strip().lower()

#command
command_list=["s","a","d","u","q"]

#add function
def Show_Skill():
    cr.execute(f"select * from skills Where user_id = {uid}")
    result=cr.fetchall()
    print(f"you have {len(result)} skill")
    if len(result)>0:
       print(f"showing skill with progrss: ")
    for row in result:
        print(f"your skill is {row[0]}=> progress is {row[1]} %")
    commit_and_close()

def Add_Skill():
    sk=input("Write YOur Skill: ").strip().capitalize()
    cr.execute(f"select name from skills Where name = '{sk}' and user_id = {uid}")
    result=cr.fetchone()
    if result == None:
        # print("skill not exist")
        prog=input("Write Your Progress: ")
        cr.execute(f"insert into skills (name ,progress,user_id) values('{sk}','{prog}','{uid}')")
    else :
        # print("th skill is exist")
        upd=input("the skill is exist, do you need to update y or n ?")
        if upd == "y":
            #  sk=input("Write YOur Skill: ").strip().capitalize()
             newprog=input("write new progress")
             cr.execute(f"update skills set progress = '{newprog}' Where name = '{sk}' and user_id = {uid}")
             print("progress is updated")
        else :
            print("ok")

    commit_and_close()

def Delete_Skill():
    sk=input("Write YOur Skill: ").strip().capitalize()
    cr.execute(f"delete from skills where name = '{sk}' and user_id = '{uid}'")
    commit_and_close()
def Update_Skill_Progress():
    sk=input("Write YOur Skill: ").strip().capitalize()
    newprog=input("write new progress")
    cr.execute(f"update skills set progress = '{newprog}' Where name = '{sk}' and user_id = {uid}")
    print("progress is updated")
    # result=cr.fetchone()

    # print(f"you have {len(result)} skill")
    commit_and_close()
#check commend list exist
if user_input in command_list:
    # print(f"command \"{user_input}\" found")
    if user_input == "s":
         Show_Skill()
         
    elif user_input == "a":
         Add_Skill()

    elif user_input == "d":
        Delete_Skill()

    elif user_input == "u":
        Update_Skill_Progress()

    else :
       print("app closed")
else:
    print(f"command \"{user_input}\"  not found")
