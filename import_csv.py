
import sqlite3
import csv

# HEADER HAS BEEN IGNORED
connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()

def import_csv():
    data_list = []

    with open('capstone_example.csv', 'r') as csvfile:
        data = csv.reader(csvfile)
        header = next(data)

        insert_sql = "INSERT INTO Assessment_Results (user_id, assess_name, score, date_taken, time_taken, manager) VALUES(?, ?, ?, ?, ?, ?);"

        if header != None:
            for row in data:
                data_list.append(row)
                print(data_list)

        cursor.executemany(insert_sql, data_list)

        connection.commit()

import_csv()
        
        



