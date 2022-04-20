import sqlite3
from passlib.hash import sha256_crypt


connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()  
from login import login
from addfunc import add_competency, add_user, add_assessment, add_assessment_results
from viewfunc import view_all_users, search_for_user,view_competencies_user, view_level_report_user, view_comp_report, view_user_comp_assess,view_user_assessments_list
from infofunctions import user_info
from editfunc import edit_competencies, edit_user, edit_assessment, edit_assessment_result,manager_edit_user
from import_csv import import_csv
from export import competency_lists_export, user_lists_export
print("\n\n---Competency Assessment Database---")


while True:
    main_menu = input("          --Main Menu-- \n\n [1] Login \n [2] Quit \n\n")  
    if main_menu == '1':
        login_user_info = login()
        user_type = login_user_info[0]
        user_id = login_user_info[1]
        while True:              
            if user_type == 'user':
                user_menu = input("\n-- User Menu -- \n\n Please choose from the following menu options:\n\n [1] View Your Assessments And Competencies \n [2] Edit Account Information \n [3] Quit \n\n")
                if user_menu == '1':
                    view_user_comp_assess(user_id)
                    
                if  user_menu == '2':
                    user_info(user_id)
                    edit_user(user_id)

                elif user_menu == '3':
                    break
                
            elif user_type == 'manager':
                menu = input('\n --Manager Menu-- \n\nPlease choose from the following menu options: \n\n [1] Users\n [2] Competencies \n [3] Assessment Results \n [4] Quit \n\n')
                if menu == '1':
                    manager_menu = input('\nPlease select from the following options: \n [1] View users \n [2] Search for a user \n [3] Add A New User \n [4] View User Competencies  \n [5] View Users Competency Assessment Results \n [6] Edit User Information\n\n ')
                    if manager_menu == '1':
                        view_all_users()
                        
                    
                    if manager_menu == '2':
                        search_for_user()
                    
                    
                    if manager_menu == '3':
                        add_user()
                    
                    
                    if manager_menu == '4':
                        view_competencies_user()
                        
                    
                    if manager_menu == '5':
                        view_level_report_user()
                        
                    
                    if manager_menu == '6':
                        manager_edit_user(user_id)

                    if manager_menu == '7':
                        user_lists_export()
                        
                        
                while menu == '2':
                    comp_menu = input('Please select from the following options: \n\n [1] View Users Competency Level Report \n [2] Add A Competency \n [3] Edit A Competency \n [4] Export Competencies List \n [5] Quit \n\n')
                    if comp_menu == '1':
                       
                        view_comp_report()
                        
                    if comp_menu == '2':
                        add_competency()
                        
                        
                        
                    if comp_menu == '3':
                        edit_competencies()
                        
                       
                    if comp_menu == '4':
                        competency_lists_export()


                    if comp_menu == '5':
                        break
 
                while menu == '3':
                    assess_menu = input('Please choose from the following options\n\n [1] View List Of Assessments \n [2] Add A Assessment \n [3] Add Assessment Results \n [4] Import CSV For Assessment Results \n [5] Edit An Assessment \n [6] Edit An Assessment Result \n [7] Quit \n\n ')
                    if assess_menu == '1':
                        view_user_assessments_list()
                    if assess_menu == '2':
                        add_assessment()
                    if assess_menu == '3':
                        add_assessment_results()
                    if assess_menu == '4':
                        import_csv()    
                    if assess_menu == '5':
                        edit_assessment()
                    if assess_menu == '6':
                        edit_assessment_result(user_id)
                    if assess_menu == '7':
                        break

                if menu == '4':
                    print("Goodbye!")
                    break        











