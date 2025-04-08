from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import mainmenu
import newUser
import testClass
import sqlite3
import os



def construct_the_database(curr):
    user_table = """CREATE TABLE IF NOT EXISTS user_table (
        id INT NOT NULL,
        userName VARCHAR(200) NOT NULL,
        PRIMARY KEY(id)
    );"""

    test_table_temp = """CREATE TABLE IF NOT EXISTS {} (
        test_id INT NOT NULL,
        relativePath VARCHAR(1000) NOT NULL,
        result VARCHAR(255),
        date DATE NOT NULL,
        user_id INT NOT NULL,
        PRIMARY KEY(test_id),
        FOREIGN KEY (user_id) REFERENCES user_table(id)
    );"""

    curr.execute(user_table)
    curr.execute(test_table_temp.format("alzheimer_test_table"))
    curr.execute(test_table_temp.format("brain_tests_table"))
    curr.execute(test_table_temp.format("diabetes_tests_table"))


conn = sqlite3.connect("HealthcareDB.db")
curr = conn.cursor()
construct_the_database(curr)

DOC_TYPES = {"Brain MRI Test":"image", 
             "Lung MRI Disease Test":"image", 
             "Alzeihmer Test":"image",
             "Diabetes": "csv",
             "Gene Test": "csv"}


app = QtWidgets.QApplication(sys.argv)
query_1 = mainmenu.main(app)


if query_1 == 1:
    new_user_info = newUser.main(app)
    user_name = new_user_info[0]
    test_type = new_user_info[1]
    path = testClass.main(app, 
                          test_type, 
                          user_name, 
                          DOC_TYPES[test_type])
    query = """SELECT id FROM user_table 
                WHERE userName = '{user_name}';"""
    result = curr.execute(query).fetchall()
    if len(result) == 0:
        insert_user = """INSERT TABLE user_table userName 
                        VALUES ({})""".format(user_name)
        curr.execute(insert_user)
    

conn.commit()
conn.close()
    
    
    

    


