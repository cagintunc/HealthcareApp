from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import mainmenu
import newUser
import testClass
import testResultGUI
import searchUser
import newUserInfo
import sqlite3
import os
import shutil
import torch
import cv2
import torch.nn.functional as F
from datetime import date


def construct_the_database(curr):
    user_table = """CREATE TABLE IF NOT EXISTS user_table (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        userName VARCHAR(200) NOT NULL,
        age INTEGER NOT NULL,
        gender VARCHAR(100) NOT NULL,
        employment VARCHAR(200) NOT NULL
    );"""

    test_table_temp = """CREATE TABLE IF NOT EXISTS {} (
        test_id INTEGER PRIMARY KEY AUTOINCREMENT,
        relativePath VARCHAR(1000) NOT NULL,
        result VARCHAR(255),
        confidence INT NOT NULL,
        date DATE NOT NULL,
        user_id INT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES user_table(id)
    );"""

    curr.execute(user_table)
    curr.execute(test_table_temp.format("alzheimer_test_table"))
    curr.execute(test_table_temp.format("brain_tests_table"))
    curr.execute(test_table_temp.format("diabetes_tests_table"))
    curr.execute(test_table_temp.format("lung_tests_table"))

def get_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (64, 64))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    image = image / 255.0
    return image


if not os.path.exists("database"):
    os.mkdir("database")

conn = sqlite3.connect("database/HealthcareDB.db")
curr = conn.cursor()
construct_the_database(curr)


DOC_TYPES = {"Brain MRI Test":["image", 
                               "../../Machine Learning/models/brain_1.pth", 
                               "brain_tests_table",
                               {0: "GLIOMA", 
                                1: "MENINGIOMA", 
                                2:"NO TUMOR", 
                                3: "PITUITARY"}], 
             "Lung MRI Disease Test":["image", 
                                      "../../Machine Learning/models/lung_1.pth", 
                                      "lung_tests_table", 
                                      {0: "NORMAL",
                                       1: "COVID19", 
                                       2: "PNEUMONIA"}], 
             "Alzeihmer Test":["image", 
                               "../../Machine Learning/models/alzh_1.pth", 
                               "alzheimer_test_table",
                               {0:"Mild Demented", 
                                1:"Moderate Demented", 
                                2:"Non-demented", 
                                3:"Very Mild Demented"}],
             "Diabetes": ["csv", 
                          None, 
                          "diabetes_tests_table"],
             "Gene Test": ["csv", 
                           None]}

app = QtWidgets.QApplication(sys.argv)
query_1 = mainmenu.main(app)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

if query_1 == 1:
    new_user_info = newUser.main(app)
    user_name = new_user_info[0]
    test_type = new_user_info[1]
    query = """SELECT id FROM user_table 
                WHERE userName = '{}';""".format(user_name)
    result = curr.execute(query).fetchall()
    if len(result) == 0:
        result = newUserInfo.main(app, user_name)
        insert_user = """INSERT INTO user_table (userName, age, gender, employment) 
                        VALUES ('{}', {}, '{}', '{}')""".format(user_name, 
                                                                result[1],
                                                                result[2],
                                                                result[3])
        curr.execute(insert_user)
    
    path = testClass.main(app, 
                          test_type, 
                          user_name, 
                          DOC_TYPES[test_type][0])

    relative_path = f"database/{user_name}"
    if not os.path.exists(relative_path):
        os.mkdir(relative_path)
    
    test_last_path = path.split("/")[-1]
    second_part = str(len(os.listdir(relative_path))) +"."+ test_last_path.split(".")[1]
    test_path = relative_path + "/" + test_last_path.split(".")[0] + second_part
    shutil.copyfile(path, test_path)
    # result
    model = torch.load(DOC_TYPES[test_type][1])
    model.to(device)
    # save the test to the database
    data = None
    if DOC_TYPES[test_type][0] == "image":
        image = get_image(test_path)
        tensor = torch.tensor(image).unsqueeze(0).unsqueeze(0).float()
        tensor = tensor.to(device)
        with torch.no_grad():
            output = model(tensor)
            probabilities = F.softmax(output, dim=1)
            predicted_class = torch.argmax(output, dim=1).item()
            confidence_level = probabilities[0][predicted_class].item()
            query = """SELECT id FROM user_table 
                    WHERE userName = '{}';""".format(user_name)
            result = curr.execute(query).fetchall()
            user_id = result[0] 
            today_date = date.today().strftime('%Y-%m-%d')
            final_result = DOC_TYPES[test_type][3][predicted_class]
            insert_test = """INSERT INTO {} 
            (relativePath, result, confidence, date, user_id) 
            VALUES ('{}', '{}', {}, '{}', {});""".format(DOC_TYPES[test_type][2], 
                                    test_path, 
                                    final_result,
                                    int(confidence_level*100),
                                    today_date,
                                    user_id[0])
            
            curr.execute(insert_test)
            
            end_point_for_results = [test_type, today_date, final_result]
            testResultGUI.main(app, user_name, end_point_for_results)

elif query_1 == 0:
    returned_data = searchUser.main(app, curr)
    testResultGUI.main(app, returned_data[0], returned_data[1])
            

conn.commit()
conn.close()
sys.exit(0)    
    
    

    


