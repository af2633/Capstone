import sqlite3
import pwinput
from passlib.hash import sha256_crypt 


connection = sqlite3.connect('capstone.db')

cursor = connection.cursor()


def login():
    
    user_name = input("Please Enter Username \n")
    password = pwinput.pwinput("Please Enter Password \n")
    user_type = 'default'
    user_id = 'default'

    query = "SELECT email, password, user_type, user_id, first_name FROM Users WHERE email = ?"
    user_info = cursor.execute(query,[user_name]).fetchone()
    

    
    try:
        password2 = user_info[1]
        if  sha256_crypt.verify(password, password2):
            user_type = user_info[2]
            user_id = user_info[3]
            first_name = user_info[4]        
            print("  Welcome "+ first_name)
        else:
            print("Incorrect Password")
            
    except:
        print("Incorrect Username")
        user_name = input("Please Enter Username \n")
        password = pwinput.pwinput("Please Enter Password \n")
        

    connection.commit()
    return user_type, user_id

    
    
# login()