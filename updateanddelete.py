import sqlite3
db=sqlite3.connect("app.db")
cr=db.cursor()

#update
cr.execute("update users set name ='sayed' where user_id = 1")
cr.execute("update users set name ='mohsen' where user_id = 2")
cr.execute("update users set name ='abdo' where user_id = 3")
#delete
cr.execute("delete from users where user_id= 3")

# fetch to data
cr.execute("select * from users")
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())
#save
# db.commit()