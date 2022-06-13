'''import sqlite3

from sqlite3 import Error
 
def sql_connection():
 
    try:
 
        con = sqlite3.connect('mydatabase1.db')
 
        return con
 
    except Error:
 
        print(Error)
 
def sql_table(con):
 
    
    table1 = "CREATE TABLE employ(id integer PRIMARY KEY, name text, salary real,department text, position text, hireDate text)"
    table2 = "CREATE TABLE employe(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)"
    for i in [table1,table2]:
        print(i)
        cursorObj = con.cursor()
        cursorObj.execute(i)

        con.commit()
 
con = sql_connection()
 
sql_table(con)'''

'''import sqlite3
 
con = sqlite3.connect('mydatabase1.db')
 
def sql_insert(con, entities):
 
    cursorObj = con.cursor()
    
    cursorObj.execute('INSERT INTO employ(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
    
    con.commit()
 
entities0 = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
 
entities1 = (3, 'ert', 800, 'ITI', 'Tech', '2018-02-06')
 
entities2 = (4, 'tre', 800, 'IIT', 'Tech', '2018-02-06')
 
entities3 = (5, 'sdf', 800, 'IWT', 'Tech', '2018-02-06')

for entities in [entities0,entities1,entities2,entities3]:
    sql_insert(con, entities)'''



'''import sqlite3
 
con = sqlite3.connect('mydatabase1.db')
 
def sql_update(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('UPDATE employ SET name = "Rogers" where id = 2')
 
    con.commit()
 
sql_update(con)'''

'''import sqlite3
 
con = sqlite3.connect('mydatabase1.db')
 
def sql_fetch(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('SELECT * FROM employ')
 
    rows = cursorObj.fetchall()
    print(rows)
 
    for row in rows:
 
        print(row)
 
sql_fetch(con)'''

import sqlite3
import random
import getpass

    

def registration(cur):
    user = input ("Username:")
    pswd = input("Password:")
    cursor = cur.cursor()
    
    cursor.execute('INSERT INTO usercredentials(username, password) VALUES(?, ?)', (user,pswd))
    cur.commit()
 
    
def login(cur):
    
    cursor = cur.cursor()
    user = input ("Username")    
    pswd = input("Password:")
    cursor.execute('SELECT * from usercredentials WHERE username="%s" AND password="%s"' % (user, pswd))
    if cursor.fetchone() is not None:
        print ("Welcome Ur OTP:",random.randint(999,10000))
    else:
        print ("Login failed")
 

def updatepassword(cur):

    cursor = cur.cursor()
    user = input ("Username")
    pswd = input("Password:")      
    cursor.execute('SELECT * from usercredentials WHERE username="%s" AND password="%s"' % (user, pswd))
        
                   
    if cursor.fetchone() is not None:
        pswd = input("Enter new password :") 
        cursor.execute('UPDATE usercredentials SET password="%s" where username="%s"'% (pswd,user))
        
        
        
    else:
        print ("Login failed")

def deleteUser(cur):

    cursor = cur.cursor()
    user = input ("Username")
    pswd = input("Password:")      
    cursor.execute('SELECT * from usercredentials WHERE username="%s" AND password="%s"' % (user, pswd))
        
                   
    if cursor.fetchone() is not None:
        
        cursor.execute('DELETE FROM usercredentials WHERE username="%s"' % (user))
        print ('"%s" deleted from DataBase'%(user))              
        
    else:
        print ("Login failed")
        
def deleteTable(cur):
    cursor = cur.cursor()
    user = input ("Username")
    pswd = input("Password:")      
    cursor.execute('DROP TABLE usercredentials ')
        
  
    
    

def main():
    
    mode = int (input("Enter 1 for registration\n Enter 2 for login\n and 3 for updatepassword"))
    db = sqlite3.connect('login.db')
    c = db.cursor()
    c.execute('create table if not exists usercredentials \
              (ID INTEGER PRIMARY KEY AUTOINCREMENT, username text NOT NULL, password text NOT NULL);')
    
    if mode ==1:
        registration(db)
    elif mode ==2:
        login(db)
    elif mode == 3:
        updatePassword(db)
    elif mode == 4:
        deleteUser(db)
    elif mode == 5:
        deleteTable(db)
    else:
        print("enter valid mode")
    #cursor.close()
    
    db.commit()
    db.close()
    
if __name__ == '__main__':
    main()








































