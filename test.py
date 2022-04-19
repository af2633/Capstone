import sqlite3
from passlib.hash import sha256_crypt 

connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()


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
    
    connection.commit()
manager_edit_user(17)
    





# # def add_competency():
# print('\n--- Add a Competency ---\n')


# name = input("Please enter a new competency name:\n")

# date_created = input("Please enter todays date: (YYYY-MM-DD)\n")

# rows = "INSERT INTO Competencies (comp_name, date_created) VALUES (?,?)"
# values = (name, date_created)
# print("Competency Has Been Added")
# cursor.execute(rows, [values])

# connection.commit()
#     # add_competency()






#NEED TO TAKE OUT UPDATE ASSESSMENT RESULTS ASSESS_NAME

# def edit_assessment_result():
#     user = ''
#     menu = input("\n Please enter the number for the field you want to update\n [1] Score \n [2] Date Taken \n [3] Time Taken  \n To delete an assessment result type delete \n ")
#     if menu == '':
#         pass
#     if menu == '1':
#         user_id = input('Please enter User ID \n')
#         date_taken = input('Please enter the date the assessment was taken\n')
#         assess_name = input('Please enter most recent assessment name \n')
#         score = input('Please enter the users assessment result score 0-4 \n')
#         user = 'UPDATE Assessment_Results SET score = ? WHERE user_id = ? AND assess_name = ? AND date_taken =?'
#         cursor.execute(user, [score,user_id, assess_name, date_taken])
#         connection.commit()
#     if menu == '2':
#         user_id = input('Please enter User ID \n')
#         assess_name = input('Please enter the assessment name\n')
#         date = input('Please enter the date the assessment was taken YYYY-MM-DD \n')
#         newdate = input('Please enter new date: \n')
#         user = 'UPDATE Assessment_Results SET date_taken = ? WHERE user_id = ? AND assess_name = ? AND date_taken =?'
#         cursor.execute(user, [newdate, user_id, assess_name, date])
#         connection.commit()
#     if menu == '3':
#         user_id = input('Please enter User ID \n')
#         assess_name = input('Please enter the most recent assessment name\n')
#         date_taken = input('Please enter the date the assessment was taken\n')
#         time_taken =  input('Please enter the new time taken hh:mm:ss\n')
#         user = 'UPDATE Assessment_Results SET time_taken = ? WHERE user_id = ? AND assess_name =? AND date_taken =?'
#         cursor.execute(user, [time_taken, user_id, assess_name, date_taken])
#         connection.commit()
#     if  menu == 'delete'.lower():
#         user_id = input('Please enter User ID\n')
#         assess_name = input('Please enter the assessment name\n')
#         date_taken = input('Please enter the date taken\n')
#         delete_assessment_result(user_id)
    
# edit_assessment_result()
# connection.commit()


# # THIS FUNCTION IS DELETES ASSESSMENT RESULTS OUT OF THE DATABASE FOR A MANAGER
# def delete_assessment_result(user_id, assess_name, date_taken):
#     user = 'DELETE FROM Assessments_Results WHERE user_id=? AND assess_name = ? AND date_taken = ?'
#     print("Assessment Results have been deleted")
#     cursor.execute(user,[user_id, assess_name, date_taken])

#     connection.commit()

# def edit_assessment():

#     menu = input("\n Please enter the number for the field you want to update\n [1] Edit Assessment name \n [2] Edit Competency \n [3] Edit Date Created \n")
#     if menu == '':
#         pass
#     if menu == '1':
#         my_values = input('Please enter most recent Assessment name: \n')
#         assess= input('Please Enter New Assessment Name \n')
#         query = 'Update Assessments SET assess_name = ? WHERE assess_name = ?'
#         cursor.execute(query, [assess, my_values])
#         query1 = 'Update Assessment_Results SET assess_name = ? WHERE assess_name = ?'
#         cursor.execute(query1, [assess, my_values])
#         connection.commit()
#     if menu == '2':
#         my_values = input('Please enter original competency name \n')
#         comp_name = input('Please enter new competency name \n')
#         query3 = 'UPDATE Assessments SET comp_name = ? WHERE comp_name = ?'
#         cursor.execute(query3, [comp_name, my_values])
#         connection.commit()
#     if menu == '3':
#         my_values = input ('Please enter the assessment name:\n')
#         date_created = input('Please enter new date created \n ')
#         user = 'UPDATE Assessments SET date_created = ? WHERE  assess_name= ?'
#         cursor.execute(user, [date_created, my_values])

#         connection.commit()

# edit_assessment()

# def edit_assessment_result(user_id):
#     query = ''
#     my_values = ''
#     menu = input("\n Please enter the number for the field you want to update\n [1] Assessment \n [2] Score \n [3] Date Taken \n [4] Time Taken \n [5] Manager \n To delete an assessment result type delete \n")
#     if menu == '':
#         pass
#     if menu == '1':
#         my_values = input('Please enter assessment name:')
#         query = 'UPDATE Assessment_Results SET assess_name = ? WHERE user_id = ? AND assess_name = ?'
#         cursor.execute(query, [my_values, user_id])
#     if menu == '2':
#         my_values = input('Please enter the users assessment result score 0-4 \n')
#         query = 'UPDATE Assessment_Results SET score = ? WHERE user_id = ? AND score = ?'
#         cursor.execute(query, [my_values, user_id])
#     if menu == '3':
#         my_values =  input('Please enter the date the assessment was taken YYYY-MM-DD \n')
#         query = 'UPDATE Assessment_Results SET date_taken = ? WHERE user_id = ? AND date_taken ?'
#         cursor.execute(query, [my_values, user_id])
#     if menu == '4':
#         my_values =  input('Please enter the time the assessment was taken hh:mm:ss \n')
#         query = 'UPDATE Assessment_Results SET time_taken = ? WHERE user_id = ? And time_taken = ?'
#         cursor.execute(query, [my_values, user_id])
#     if  menu == 'delete'.lower():
#         delete_assessment_result(user_id)
    
# edit_assessment_result(3)
# connection.commit()



# # THIS FUNCTION IS DELETES ASSESSMENT RESULTS OUT OF THE DATABASE FOR A MANAGER
# def delete_assessment_result(user_id):
#     user = 'DELETE FROM Assessments_Results WHERE user_id=?'
#     print("Assessment Results have been deleted")
#     cursor.execute(user, user_id)

#     connection.commit()




# def edit_assessment_result(user_id):
#     user = ''
#     my_values = ''
#     menu = input("\n Please enter the number for the field you want to update\n [1] Assessment \n [2] Score \n [3] Date Taken \n [4] Time Taken \n [5] Manager \n To delete an assessment result type delete ")
#     if menu == '':
#         pass
#     if menu == '1':
#         my_values = input('Please enter original assessment name \n')
#         new_assess = input('Please enter new assessment name \n')
#         query = 'UPDATE Assessment_Results SET assess_name = ? WHERE user_id = ?'
#         cursor.execute(query, [my_values, user_id])
#     if menu == '2':
#         my_values = input('Please enter the users assessment result score 0-4 \n')
#         score = input('Please enter the users new assessment score 0-4 \n')
#         query = 'UPDATE Assessment_Results SET score = ? WHERE user_id = ?'
#         cursor.execute(user, [my_values, user_id])
#     if menu == '3':
#         my_values =  input('Please enter the date the original assessment was taken YYYY-MM-DD \n')
#         date_taken = input('Please enter the date the assessment was taken YYYY-MM-DD\n')
#         query = 'UPDATE Assessment_Results SET date_taken = ? WHERE user_id = ?'
#         cursor.execute(user, [my_values, user_id])
#     if menu == '4':
#         my_values =  input('Please enter the original time the assessment was taken hh:mm:ss \n')
#         time_taken = input('Please enter new time the assessment was taken \n')
#         query = 'UPDATE Assessment_Results SET time_taken = ? WHERE user_id = ?'
#         cursor.execute(user, [my_values, user_id])
#     if  menu == 'delete'.lower():
#         delete_assessment_result(user_id)
    

#     connection.commit()


# # THIS FUNCTION IS DELETES ASSESSMENT RESULTS OUT OF THE DATABASE FOR A MANAGER
# def delete_assessment_result(user_id):
#     user = 'DELETE FROM Assessments_Results WHERE user_id=?'
#     print("Assessment Results have been deleted")
#     cursor.execute(user, user_id)

#     connection.commit()


# def edit_competencies():
    
#     menu = input("\n Please enter the number for the field you want to update\n [1] competency name: \n [2] date created: ")
#     if menu == '':
#         pass
#     if menu == '1':
#         original_name = input('Please enter original competency name \n')
#         new_name = input("Please enter new competency name \n")
#         competency_name = 'UPDATE Competencies SET comp_name = ? WHERE comp_name = ?'
#         cursor.execute(competency_name, [new_name, original_name])
#     if menu == '2':
#         my_values = input('Please enter competency name \n')
#         new_date = input('Please enter most recent date \n')
#         date_created = 'UPDATE Competencies SET date_created = ? WHERE comp_name = ?'
#         cursor.execute(date_created, [new_date, my_values])
#         print("Competency Has Been Updated")

#     connection.commit()
# edit_competencies()

# def edit_assessment():
    
#     menu = input("\n Please enter the number for the field you want to update\n [1] Edit Assessment name: \n [2] Edit Competency: \n [3] Edit Date Created: \n")
#     if menu == '':
#         pass
#     if menu == '1':
#         my_values = input('Please enter most recent Assessment name:')
#         assess= input('Please Enter New Assessment Name \n')
#         query = input('Update Assessments SET assess_name = ? WHERE assess_name = ?')
#         cursor.execute(query, [assess, my_values])
#     if menu == '2':
#         my_values = input('Please enter original competency name \n')
#         comp_name = input('Please enter new competency name \n')
#         query = 'UPDATE Assessments SET comp_name = ? WHERE comp_name = ?'
#         cursor.execute(query, [comp_name, my_values])
#     if menu == '3':
#         my_values = input ('Please enter the assessment name:\n')
#         date_created = input('Please enter new date created \n ')
#         user = 'UPDATE Assessments SET date_created = ? WHERE  assess_name= ?'
#         cursor.execute(user, [date_created,my_values])

#         connection.commit()










# def competency_scale(info):
#     query = cursor.execute ("SELECT * FROM Competency_scale").fetchall()
#     info = cursor.execute(query[info]).fetchone()
#     print (f' \nScore {info[0]} ')
#     print (f' \nScore Name {info[1]} ')
#     print (f' \nScore Definition {info[2]} ')
    
# print(competency_scale)
# connection.commit()





# def view_comp_report():
# comp_name = input("Please enter competency name: ")
# print('\n--- View Competency Report ---\n')
# query = "SELECT C.comp_name, u.user_id, first_name, last_name, AR.score, score_name, date_taken FROM Users U JOIN Assessment_Results AR ON U.user_id = AR.user_id JOIN Assessments A ON AR.assess_name=A.assess_name JOIN Competencies C ON A.comp_name=C.comp_name JOIN Competency_scale CS ON AR.score=cs.score WHERE C.comp_name = ? ORDER BY U.USER_ID, DATE_TAKEN DESC"
# rows = cursor.execute(query, (f'{comp_name}',)).fetchall()
# my_list = ['comp_name', 'user_id', 'first_name', 'last_name', 'score', 'score_name']

# print (f"{'comp_name':<20}{'user_id':<20}{'first_name':<20}{'last_name':<20}{'score':<10}{'score_name':>10}") 

# for my_list in rows:
#     my_list = [str(x) for x in my_list]
#     print(f'{my_list[0]:<20}{my_list[1]:<20}{my_list[2]:<20}{my_list[3]:<20}{my_list[4]:<10}{my_list[5]:<10}')
    
#     connection.commit()



# SELECT C.comp_name, u.user_id, first_name, last_name, AR.score, score_name, date_taken FROM Users U JOIN Assessment_Results AR ON U.user_id = AR.user_id JOIN Assessments A ON AR.assess_name=A.assess_name JOIN Competencies C ON A.comp_name=C.comp_name JOIN Competency_scale CS ON AR.score=cs.score WHERE C.comp_name = ? ORDER BY U.USER_ID, DATE_TAKEN DESC

# SELECT C.comp_name, u.user_id, first_name, last_name, AR.score, score_name, date_taken FROM Users U JOIN Assessment_Results AR ON U.user_id = AR.user_id JOIN Assessments A ON AR.assess_name=A.assess_name JOIN Competencies C ON A.comp_name=C.comp_name JOIN Competency_scale CS ON AR.score=cs.score WHERE U.user_id = ?







# def edit_user(user_id):
#     user = ''
#     my_values = ''
#     menu = input("\n Please enter the number for the field you want to update\n [1] first name: \n [2] last name: \n [3] password: \n")
#     if menu == '':
#         pass
#     if menu == '1':
#         my_values = input('Please enter first name: ')
#         user = 'UPDATE Users SET first_name = ? WHERE user_id = ?'
#         cursor.execute( user, [my_values, user_id])
#     if menu == '2':
#         my_values = input('Please enter last name: ')
#         user = 'UPDATE Users SET last_name = ? WHERE user_id = ?'
#         cursor.execute( user, [my_values,user_id])
#     if menu == '3':
#         my_values = sha256_crypt.encrypt(input('Please enter new password: '))
#         user = 'UPDATE Users SET password = ? WHERE user_id = ?'
#         cursor.execute( user, [my_values, user_id])
  
    
#     connection.commit()
# edit_user(7)

# def view_level_report_user():
# print('\n--- View A Users Level Report ---\n')
# user_id = input("Please enter user_id: ")
# query = "SELECT u.user_id, first_name, last_name, assess_name, AR.score, score_name, date_taken, manager FROM Users U JOIN Assessment_Results AR ON U.user_id = AR.user_id JOIN Assessments A ON AR.assess_name=A.assess_name JOIN Competencies C ON A.comp_name=C.comp_name JOIN Competency_scale CS ON AR.score=cs.score WHERE U.user_id = ?;"
# rows = cursor.execute(query, (f'{user_id}',)).fetchall()
# my_list = ['user_id', 'first_name', 'last_name', 'assess_name', 'score', 'score_name', 'date_taken', 'manager']

# print (f"{'User ID':<20}{'First Name':<20}{'Last Name':<20}{'Assessment Name':<35}{'Score':<10}{'Score Name':>10}{'Date Taken':>10}{'Manager':>10}") 

# for my_list in rows:
#     my_list = [str(x) for x in my_list]
#     print(f'{my_list[0]:<20}{my_list[1]:<20}{my_list[2]:<20}{my_list[3]:<35}{my_list[4]:<10}{my_list[5]:<10}{my_list[6]:<10}{my_list[7]:<10}')
    
    # connection.commit()

# def view_level_report_user():
# print('\n--- View All Users Competencies By User ---\n')
# user_id = input("Please enter user_id: ")
# query = ("SELECT u.user_id, first_name, last_name, C.comp_name, Ar.score, score_name, score_def, AR.assess_name, AR.date_taken FROM Users U JOIN Assessment_Results AR ON U.user_id = AR.user_id JOIN Assessments A ON AR.assess_name=A.assess_name JOIN Competencies C ON A.comp_name=C.comp_name JOIN Competency_scale CS ON AR.score=cs.score WHERE U.user_id = ?")
# rows = cursor.execute(query, (f'{user_id}',)).fetchall()
# my_list = ['User ID', 'First Name', 'Last Name', 'Competency Name', 'Score', 'Score Name', 'Score Definition', 'Assessment Name', 'Date Taken']

# print (f"{'User ID':<10}{'First Name':<20}{'Last Name':<20}{'Competency Name':<20}{'score':<10}{'score_name':<20}{'Score Definition':<35}{'Assessment Name':<40}{'Date Taken':<10}") 

# for my_list in rows:
#     my_list = [str(x) for x in my_list]
#     print(f'{my_list[0]:<10}{my_list[1]:<20}{my_list[2]:<20}{my_list[3]:<20}{my_list[4]:<10}{my_list[5]:<20}{my_list[6]:<35}{my_list[7]:<40}{my_list[8]:<10}')
    
#     connection.commit()

    # def view_all_users():
    # rows = cursor.execute("SELECT user_id, first_name, last_name, phone_number, email FROM Users").fetchall()
    # my_list = [ 'user_id', 'first_name', 'last_name', 'phone_number', 'email']
    # print (f"{'user_id':<15}{'first_name':<25}{'last_name':<20}{'phone_number':<18}{'email':15}\n") 

    # for my_list in rows:
    #     my_list = [str(x) for x in my_list]
    #     print(f'{my_list[0]:<15}{my_list[1]:<25}{my_list[2]:<20}{my_list[3]:<18}{my_list[4]:<15}')
        
    #     connection.commit()





#THIS ON IS VERY CONFUSING STILL NOT FINISHED

# def view_comp_report():
#     comp_name = input("Please enter competency name: ")
#     print('\n--- View Competency Report ---\n')
#     query = "SELECT C.comp_name, u.user_id, first_name, last_name, score FROM Users U JOIN Assessment_Results AR ON U.user_id = AR.user_id JOIN Assessments A ON AR.assessment=A.assess_name JOIN Competencies C ON A.competency=C.comp_name WHERE C.comp_name =?"
#     rows = cursor.execute(query, (f'{comp_name}',)).fetchall()
#     my_list = ['comp_name', 'user_id', 'first_name', 'last_name', 'score']
    
#     print (f"{'comp_name':<15}{'user_id':<25}{'first_name':<20}{'last_name':<25}{'score':<10}") 

#     for my_list in rows:
#         my_list = [str(x) for x in my_list]
#         print(f'{my_list[0]:<15}{my_list[1]:<25}{my_list[2]:<20}{my_list[3]:<25}{my_list[4]:<10}')
        
#         connection.commit()
# view_comp_report()



# def edit_assessment_result(user_id):
#     user = ''
#     my_values = ''
#     menu = input("\n Please enter the number for the field you want to update\n [1] Assessment: \n [2] Score: \n [3] Date Taken: \n [4] Time Taken: \n [5] Manager: \n To delete an assessment result type delete: ")
#     if menu == '':
#         pass
#     if menu == '1':
#         my_values = input('Please enter assessment name:')
#         user = f'UPDATE Assessment_Results SET assessment = ? WHERE user_id = {user_id};'
#         cursor.execute(user, [my_values])
#     if menu == '2':
#         my_values = input('Please enter the users assessment result score 0-4:')
#         user = f'UPDATE Assessment_Results SET score = ? WHERE user_id = {user_id};'
#         cursor.execute(user, [my_values])
#     if menu == '3':
#         my_values =  input('Please enter the date the assessment was taken YYYY-MM-DD:')
#         user = f'UPDATE Assessment_Results SET date_taken = ? WHERE user_id = {user_id}'
#         cursor.execute(user,[my_values])
#     if menu == '4':
#         my_values =  input('Please enter the time the assessment was taken hh:mm:ss')
#         user = f'UPDATE Assessment_Results SET time_taken = ? WHERE user_id = {user_id}'
#         cursor.execute(user,[my_values])

#     connection.commit()

# edit_assessment_result(1)

