import sqlite3
from passlib.hash import sha256_crypt 

connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()

# THIS FUNCTION IS FOR THE USER TO BE ABLE TO EDIT PERSONAL INFORMATION
def edit_user(user_id):
    user = ''
    my_values = ''
    menu = input("\n Please enter the number for the field you want to update: \n [1] First Name \n [2] Last Name \n [3] Password \n")
    if menu == '':
        pass
    if menu == '1':
        my_values = input('Please enter first name: ')
        user = 'UPDATE Users SET first_name = ? WHERE user_id = ?'
        cursor.execute( user, [my_values, user_id])
    if menu == '2':
        my_values = input('Please enter last name: ')
        user = 'UPDATE Users SET last_name = ? WHERE user_id = ?'
        cursor.execute(user, [my_values,user_id])
    if menu == '3':
        my_values = sha256_crypt.encrypt(input('Please enter new password: '))
        user = 'UPDATE Users SET password = ? WHERE user_id = ?'
        cursor.execute(user, [my_values, user_id])
    # print(user_id)

    connection.commit()



# THIS FUNCTION IS FOR THE MANAGER TO BE ABLE TO EDIT PERSONAL INFO

def manager_edit_user(user_id):
    user = ''
    my_values = ''
    menu = input("\n Please enter the number for the field you want to update\n [1] first name \n [2] last name \n [3] phone number \n [4] email \n [5] password \n ")
    if menu == '':
        pass
    if menu == '1':
        my_values = input('Please enter first name \n ')
        user = 'UPDATE Users SET first_name = ? WHERE user_id = ?'
        cursor.execute(user, [my_values, user_id])
    if menu == '2':
        my_values = input('Please enter last name \n')
        user = 'UPDATE Users SET last_name = ? WHERE user_id = ?'
        cursor.execute(user, [my_values,user_id])
    if menu == '3':
        my_values = input('Please enter phone number \n')
        user = 'UPDATE Users SET phone_number = ? WHERE user_id = ?'
        cursor.execute(user, [my_values, user_id])
    if menu == '4':
        my_values = input('Please enter email address \n')
        user = 'UPDATE Users SET email = ? WHERE user_id = ?'
        cursor.execute(user, [my_values, user_id])
    if menu == '5':
        my_values = sha256_crypt.encrypt(input('Please enter new password \n '))
        user = 'UPDATE Users SET password = ? WHERE user_id = ?'
        cursor.execute(user, [my_values, user_id])
    print(user_id)

    connection.commit()


#DONE!!!
def edit_competencies():
    
    menu = input("\n Please enter the number for the field you want to update\n [1] competency name \n [2] date created \n ")
    if menu == '':
        pass
    if menu == '1':
        original_name = input('Please enter original competency name \n')
        new_name = input("Please enter new competency name \n")
        competency_name = 'UPDATE Competencies SET comp_name = ? WHERE comp_name = ?'
        cursor.execute(competency_name, [new_name, original_name])
    if menu == '2':
        my_values = input('Please enter competency name \n')
        new_date = input('Please enter most recent date \n')
        date_created = 'UPDATE Competencies SET date_created = ? WHERE comp_name = ?'
        cursor.execute(date_created, [new_date, my_values])
        print("Competency Has Been Updated")

    connection.commit()
# edit_competencies()



#THIS ONE IS DONE
def edit_assessment():

    menu = input("\n Please enter the number for the field you want to update\n [1] Edit Assessment name \n [2] Edit Competency \n [3] Edit Date Created \n")
    if menu == '':
        pass
    if menu == '1':
        my_values = input('Please enter original Assessment name: \n')
        assess= input('Please Enter New Assessment Name \n')
        query = 'Update Assessments SET assess_name = ? WHERE assess_name = ?'
        cursor.execute(query, [assess, my_values])
        query1 = 'Update Assessment_Results SET assess_name = ? WHERE assess_name = ?'
        cursor.execute(query1, [assess, my_values])
        connection.commit()
    if menu == '2':
        my_values = input('Please enter original competency name \n')
        comp_name = input('Please enter new competency name \n')
        query3 = 'UPDATE Assessments SET comp_name = ? WHERE comp_name = ?'
        cursor.execute(query3, [comp_name, my_values])
        connection.commit()
    if menu == '3':
        my_values = input ('Please enter the assessment name:\n')
        date_created = input('Please enter new date created \n ')
        user = 'UPDATE Assessments SET date_created = ? WHERE  assess_name= ?'
        cursor.execute(user, [date_created,my_values])

        connection.commit()




#NEED TO TAKE OUT UPDATE ASSESSMENT RESULTS ASSESS_NAME

def edit_assessment_result():
    user = ''
    menu = input("\n Please enter the number for the field you want to update\n [1] Score \n [2] Date Taken \n [3] Time Taken  \n To delete an assessment result type delete ")
    if menu == '':
        pass
    if menu == '1':
        user_id = input('Please enter User ID \n')
        date_taken = input('Please enter the date the assessment was taken\n')
        assess_name = input('Please enter most recent assessment name \n')
        score = input('Please enter the users assessment result score 0-4 \n')
        user = 'UPDATE Assessment_Results SET score = ? WHERE user_id = ? AND assess_name = ? AND date_taken =?'
        cursor.execute(user, [score,user_id, assess_name, date_taken])
        connection.commit()
    if menu == '2':
        user_id = input('Please enter User ID \n')
        assess_name = input('Please enter the assessment name\n')
        date = input('Please enter the date the assessment was taken YYYY-MM-DD \n')
        newdate = input('Please enter new date: \n')
        user = 'UPDATE Assessment_Results SET date_taken = ? WHERE user_id = ? AND assess_name = ? AND date_taken =?'
        cursor.execute(user, [newdate, user_id, assess_name, date])
        connection.commit()
    if menu == '3':
        user_id = input('Please enter User ID \n')
        assess_name = input('Please enter the most recent assessment name\n')
        date_taken = input('Please enter the date the assessment was taken\n')
        time_taken =  input('Please enter the new time taken hh:mm:ss\n')
        user = 'UPDATE Assessment_Results SET time_taken = ? WHERE user_id = ? AND assess_name =? AND date_taken =?'
        cursor.execute(user, [time_taken, user_id, assess_name, date_taken])
        connection.commit()
    if  menu == 'delete'.lower():
        user_id = input('Please enter User ID\n')
        assess_name = input('Please enter the assessment name\n')
        date_taken = input('Please enter the date taken\n')
        delete_assessment_result(user_id)
    

    connection.commit()


# THIS FUNCTION IS DELETES ASSESSMENT RESULTS OUT OF THE DATABASE FOR A MANAGER
def delete_assessment_result(user_id, assess_name, date_taken):
    user = 'DELETE FROM Assessments_Results WHERE user_id=? AND assess_name = ? AND date_taken = ?'
    print("Assessment Results have been deleted")
    cursor.execute(user,[user_id, assess_name, date_taken])

    connection.commit()
     
