
import sqlite3
import csv



connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()

def user_lists_export():
    rows = cursor.execute("SELECT * FROM Users").fetchall()
    with open('capstone.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["User ID", 'First Name', 'Last Name', 'Phone Number', 'Email', 'Password', 'Active', 'Date Created', 'Hire Date', 'User Type'])
        writer.writerows(rows)
        

user_lists_export()




def competency_lists_export():
    rows = cursor.execute("SELECT * FROM Competencies").fetchall()
    with open('capstone.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Competency Name", 'Date Created'])
        writer.writerows(rows)
        

competency_lists_export()








# def_user_list():

# cursor.execute("SELECT * FROM Users WHERE user_id = {user_id}")

# rows = cursor.fetchall()

# csv_write =  open('capstone.csv', 'w')

# for row in rows:
# .fetchall()

# with open('capstone.csv', 'w', newline='') as csvfile:
#     fields = ["SELECT * FROM Users WHERE user_id = {user_id}"]
#     writer = csv.writer(csvfile)
   
#     writer.writerows(fields) 
#     writer.writeheader() 
#     for rows in fields:  
#           writer.writerows(rows)


