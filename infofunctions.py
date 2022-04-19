import sqlite3

connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()    
    
    
    
def user_info(user_id):
    query = "SELECT user_id, first_name, last_name, phone_number, email, active, date_created, hire_date, user_type FROM Users WHERE user_id = ?"
    info = cursor.execute (query,[user_id]).fetchone()

    print ('\n---- User Information ----')
    print (' \n User ID        ' +str(info[0]))
    print (' \nFirst Name      ' +info[1])
    print (' \nLast Name       ' +info[2])
    print (' \nPhone Number    ' +info[3])
    print (' \nEmail           ' +info[4])    
    print (' \nActive          ' +str(info[5]))
    print (' \nDate Created    ' +info[6])
    print (' \nHire Date       ' +info[7])
    print (' \nUser Type       ' +info[8])

    connection.commit()



#Competencies Table???? TO PULL BY INDEX


# def competency_scale():
#     query = cursor.execute ("SELECT * FROM Competency_scale").fetchall()
#     info = cursor.execute(query).fetchone()
#     print (f' \nScore {info[0]} ')
#     print (f' \nScore Name {info[1]} ')
#     print (f' \nScore Definition {info[2]} ')
  

#     connection.commit()