import sqlite3
from passlib.hash import sha256_crypt
connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()


# Managers function

def add_user():
    print('\n--- Hello, please enter user information---\n')
    
    first_name = input("Please enter first name:\n")
    last_name = input("Please enter last name:\n")
    phone_number = input("Please enter phone number:\n")
    email = input("Please enter email:\n")
    password =  sha256_crypt.encrypt(input('Please enter new password: '))
    active = input("Please enter 1 for active or 0 if user is inactive:\n")
    date_created = input("Please enter date created:\n")
    hire_date = input("Please enter hire date:\n")
    user_type = input("Please enter user type:\n")
 
    rows = "INSERT INTO Users (first_name, last_name, phone_number, email, password, active, date_created, hire_date, user_type) VALUES (?,?,?,?,?,?,?,?,?)"
    values = [first_name, last_name, phone_number, email, password, active, date_created, hire_date, user_type]
    print("\n-- User Has Been Added --\n ")
    cursor.execute(rows, values)

    connection.commit()


def add_competency():
    print('\n--- Add a Competency ---\n')
    

    name = input("Please enter a new competency name:\n")

    date_created = input("Please enter todays date: (YYYY-MM-DD)\n")

    rows = "INSERT INTO Competencies (comp_name, date_created) VALUES (?,?)"
    values = [name, date_created]
    print("Competency Has Been Added")
    cursor.execute(rows, values)

    connection.commit()



def add_assessment():
    print('\n--- Add Assessment  ---\n')

    name = input("Please enter assessment name:\n")
    competency = input("Please enter competency:\n")
    date_created = input("Please enter date YYYY-MM-DD:\n")

    rows = "INSERT INTO Assessments (assess_name, comp_name, date_created) VALUES (?,?,?)"
    values = [name, competency, date_created]

    cursor.execute(rows, values)

    connection.commit()




# ONLY ACCESSABLE FOR MANAGER
def add_assessment_results():
    print('\n--- Add Assessment Results ---\n')
    
    user_id = input("Please enter your user ID number:\n")
    assessment = input("Please enter the Assessment Name:\n")
    score = input("Please enter your score between 0 and 4:\n")
    date_taken = input("Please enter the date the assessment was taken YYYY-MM-DD:\n")
    time_taken = input("Please enter the time the assessment was taken hh:mm:ss:\n")
    manager = input("Please enter manager ID number:\n")
    
    
    
    rows = "INSERT INTO Assessment_Results (user_id, assess_name, score, date_taken, time_taken, manager) VALUES (?,?,?,?,?,?)"
    values = [user_id, assessment, score, date_taken, time_taken, manager]
    cursor.execute(rows, values)

    connection.commit()
