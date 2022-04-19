import sqlite3

connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()



#VIEW ALL USERS

def view_all_users():
    rows = cursor.execute("SELECT user_id, first_name, last_name, phone_number, email FROM Users").fetchall()
    my_list = [ 'user_id', 'first_name', 'last_name', 'phone_number', 'email']
    print (f"{'user_id':<15}{'first_name':<25}{'last_name':<20}{'phone_number':<18}{'email':15}\n") 

    for my_list in rows:
        my_list = [str(x) for x in my_list]
        print(f'{my_list[0]:<15}{my_list[1]:<25}{my_list[2]:<20}{my_list[3]:<18}{my_list[4]:<15}\n')
        
        connection.commit()

#SEARCH FOR USER

def search_for_user():
    search_term = input('\n--- Search for a user by last name ---\n')
    query = " SELECT user_id, first_name, last_name, phone_number, email FROM Users WHERE last_name LIKE ?"
    rows = cursor.execute(query, (f'%{search_term}%',)).fetchall()
    print('\n--- Search Users ---\n')

    print (f"{'user_id':<15}{'first_name':<15}{'last_name':<20}{'phone_number':<20}{'email':<20}\n") 

    for my_list in rows:
        my_list = [str(x) for x in my_list]
        print(f'{my_list[0]:<15}{my_list[1]:<15}{my_list[2]:<20}{my_list[3]:<20}{my_list[4]:<20}\n')

    connection.commit()

# VIEW ALL USER COMPETENCIES BY USER    
    
def view_competencies_user():
    print('\n--- View All Users Competencies By User ---\n')
    user_id = input("Please enter user ID: ")
    query = ("SELECT u.user_id, first_name, last_name, C.comp_name, Ar.score, score_name, score_def, AR.assess_name, AR.date_taken FROM Users U JOIN Assessment_Results AR ON U.user_id = AR.user_id JOIN Assessments A ON AR.assess_name=A.assess_name JOIN Competencies C ON A.comp_name=C.comp_name JOIN Competency_scale CS ON AR.score=cs.score WHERE U.user_id = ?")
    rows = cursor.execute(query, (f'{user_id}',)).fetchall()
    my_list = ['User ID', 'First Name', 'Last Name', 'Competency Name', 'Score', 'Score Name', 'Score Definition', 'Assessment Name', 'Date Taken']

    print (f"{'User ID':<10}{'First Name':<20}{'Last Name':<20}{'Competency Name':<20}{'score':<10}{'score_name':<20}{'Score Definition':<35}{'Assessment Name':<40}{'Date Taken':<10}") 

    for my_list in rows:
        my_list = [str(x) for x in my_list]
        print(f'{my_list[0]:<10}{my_list[1]:<20}{my_list[2]:<20}{my_list[3]:<20}{my_list[4]:<10}{my_list[5]:<20}{my_list[6]:<35}{my_list[7]:<40}{my_list[8]:<10}\n')
        
        connection.commit()
 # DONE
def view_comp_report():
    comp_name = input("Please enter competency name: \n")
    print('\n--- View Competency Report ---\n')
    query = "SELECT C.comp_name, u.user_id, first_name, last_name, AR.score, score_name, date_taken FROM Users U JOIN Assessment_Results AR ON U.user_id = AR.user_id JOIN Assessments A ON AR.assess_name=A.assess_name JOIN Competencies C ON A.comp_name=C.comp_name JOIN Competency_scale CS ON AR.score=cs.score WHERE C.comp_name LIKE ? ORDER BY U.USER_ID, DATE_TAKEN DESC"
    rows = cursor.execute(query, [comp_name]).fetchall()
    my_list = ['comp_name', 'user_id', 'first_name', 'last_name', 'score', 'score_name']

    print (f"{'Competency Name':<20}{'User ID':<20}{'First Name':<20}{'Last Name':<20}{'Score':<10}{'Score Name':>10}") 

    for my_list in rows:
        my_list = [str(x) for x in my_list]
        print(f'{my_list[0]:<20}{my_list[1]:<20}{my_list[2]:<20}{my_list[3]:<20}{my_list[4]:<10}{my_list[5]:<10}\n')
        
        connection.commit()

# DONE

def view_level_report_user():
    print('\n--- View A Users Level Report ---\n')
    user_id = input("Please enter user_id: ")
    query = "SELECT u.user_id, first_name, last_name, AR.assess_name, AR.score, score_name, date_taken, manager FROM Users U JOIN Assessment_Results AR ON U.user_id = AR.user_id JOIN Assessments A ON AR.assess_name=A.assess_name JOIN Competencies C ON A.comp_name=C.comp_name JOIN Competency_scale CS ON AR.score=cs.score WHERE U.user_id LIKE ?"
    rows = cursor.execute(query, (f'{user_id}',)).fetchall()
    my_list = ['user_id', 'first_name', 'last_name', 'assess_name', 'score', 'score_name', 'date_taken', 'manager']

    print (f"{'User ID':<20}{'First Name':<20}{'Last Name':<20}{'Assessment Name':<45}{'Score':<15}{'Score Name':<20}{'Date Taken':<15}{'Manager':<15}") 

    for my_list in rows:
        my_list = [str(x) for x in my_list]
        print(f'{my_list[0]:<20}{my_list[1]:<20}{my_list[2]:<20}{my_list[3]:<45}{my_list[4]:<15}{my_list[5]:<20}{my_list[6]:<15}{my_list[7]:<15}\n')
        
        connection.commit()

def view_user_assessments_list():
    print('\n--- View A Users Assessment List ---\n')
    user_id = input("Please enter user_id: ")
    query = "SELECT u.user_id, first_name, last_name, C.comp_name, AR.date_taken FROM Users U JOIN Assessment_Results AR ON U.user_id = AR.user_id JOIN Assessments A ON AR.assess_name=A.assess_name JOIN Competencies C ON A.comp_name=C.comp_name JOIN Competency_scale CS ON AR.score=cs.score WHERE U.user_id LIKE ?"
    rows = cursor.execute(query, (f'{user_id}',)).fetchall()
    my_list = [ 'user_id', 'first_name', 'last_name', 'comp_name', 'date_taken']
    print (f"{'User ID':<15}{'First Name':<25}{'Last Name':<20}{'Competency Name':<18}{'Date Taken':15}\n") 

    for my_list in rows:
        my_list = [str(x) for x in my_list]
        print(f'{my_list[0]:<15}{my_list[1]:<25}{my_list[2]:<20}{my_list[3]:<18}{my_list[4]:<15}\n')
        
        connection.commit()

#THIS IS FOR THE USER TO VIEW THERE OWN COMPETENCY &ASSESSMENTS
def view_user_comp_assess(user_id):
    print('\n--- User Competencies and Assessments ---\n')
    user_id = input("Please enter your USER ID number: ")
    rows = cursor.execute("SELECT u.user_id, first_name, last_name, C.comp_name, AR.assess_name, AR.date_taken FROM Users U JOIN Assessment_Results AR ON U.user_id = AR.user_id JOIN Assessments A ON AR.assess_name=A.assess_name JOIN Competencies C ON A.comp_name=C.comp_name JOIN Competency_scale CS ON AR.score=cs.score WHERE U.user_id LIKE ?", (user_id,)).fetchall()

    print (f"{'User ID':<15}{'First Name':<25}{'Last Name':<20}{'Competency Name':<18}{'Assessment Name':<45}{'Date Taken':30}\n") 

    for my_list in rows:
        my_list = [str(x) for x in my_list]
        print(f'{my_list[0]:<15}{my_list[1]:<25}{my_list[2]:<20}{my_list[3]:<18}{my_list[4]:<45}{my_list[5]:<30}\n')
    
    connection.commit()

# extra function I can't remember what it does
# def view_level_report_user():
#     print('\n--- View A Users Level Report ---\n')
#     user_id = input("Please enter user_id: ")
#     query = "SELECT C.comp_name, u.user_id, first_name, last_name, AR.score, score_name, date_taken FROM Users U JOIN Assessment_Results AR ON U.user_id = AR.user_id JOIN Assessments A ON AR.assess_name=A.assess_name JOIN Competencies C ON A.comp_name=C.comp_name JOIN Competency_scale CS ON AR.score=cs.score WHERE U.user_id = ?"
#     rows = cursor.execute(query, (f'{user_id}',)).fetchall()
#     my_list = ['comp_name', 'user_id', 'first_name', 'last_name', 'score', 'score_name']

#     print (f"{'comp_name':<20}{'user_id':<20}{'first_name':<20}{'last_name':<20}{'score':<10}{'score_name':>10}") 

#     for my_list in rows:
#         my_list = [str(x) for x in my_list]
#         print(f'{my_list[0]:<20}{my_list[1]:<20}{my_list[2]:<20}{my_list[3]:<20}{my_list[4]:<10}{my_list[5]:<10}')
        
#         connection.commit()