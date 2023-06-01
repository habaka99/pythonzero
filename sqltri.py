import sqlite3
def get_all_data():
    try:
        #connect 
        db=sqlite3.connect("app.db")
        #
        print("database is opened succefully")
        #crusor
        cr=db.cursor()
        #incert data
        cr.execute("select * from users")
        #fetch data
        result=cr.fetchall()
        # print(result)
        #loop
        for row in result:
            print(f"user id >={row[0]}",end=" ")
            print(f"name is >={row[1]}")
    except sqlite3.Error as er:
        print (f"error is {er}")
    finally:
        if (db):
            db.close()
            print(" db is closed")
    
get_all_data()