#import sqllite
import sqlite3
#create db
db=sqlite3.connect("app.db")
# import os 
# print(os.path.abspath("app.db")  )
# cr.execute("CREATE TABLE skills (name text ,progress integer, user_id integer)")
#cursor
cr=db.cursor()
#create table 
cr.execute("create table if not exists users(user_id integer,name text) ") 
cr.execute("CREATE TABLE  if not exists skills (name text ,progress integer, user_id integer)")
#inserting data
# cr.execute("insert into users(user_id,name)values(1 ,'ahmed')")
# cr.execute("insert into users(user_id,name)values(2 ,'abdo')")
# cr.execute("insert into users(user_id,name)values(3,'mody')")
# my_list=["ahmed","sayed","abdo","mohamed","mohsen","bola"]
# for key,user in enumerate(my_list,1):
#     cr.execute(f"insert into users(user_id,name)values({key},'{user}')")
cr.execute("select user_id, name from users")
print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchmany(3))
# print(cr.fetchall())

#save(commit)
db.commit()
db.close()
