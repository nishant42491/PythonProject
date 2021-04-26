import sys
from PyQt5.QtWidgets import (QApplication,QHBoxLayout,QVBoxLayout,QWidget, QMessageBox, QPushButton, QLabel, QLineEdit)
from PyQt5.QtGui import QFont, QPixmap
import pandas as pd
import os
import mysql.connector as conn

mydb = conn.connect(host="localhost",user="root",password="root",database="shop")
mycur=mydb.cursor()



class customer:
    def __init__(self,name,surname,gender,age,username,password,idn):
        self.name=name
        self.gender=gender
        self.age=age
        self.username=username
        self.password=password
        self.surname=surname
        self.idn=idn



class CreateNewUser(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initializeUI() # Call our function used to set up window
        
    def initializeUI(self):
         """
         Initialize the window and display its contents to the screen
         """
         self.setGeometry(100, 100, 1000, 1000)
         self.setWindowTitle('3.2 - Create New User')
         self.displayWidgetsToCollectInfo()
         self.show()        

    def displayWidgetsToCollectInfo(self):
         """
         Create widgets that will be used to collect information
         from the user to create a new account.
         """
         # Create label for image
         
             
             
         title_h_box=QHBoxLayout()   
         login_label = QLabel(self)
         login_label.setText("create new account")
         title_h_box.addWidget(login_label)
         login_label.setFont(QFont('Arial', 20))
         username_h_box=QHBoxLayout()
         name_label = QLabel("username:", self)
         username_h_box.addWidget(name_label)
         
         
         self.name_entry = QLineEdit(self)
         
         self.name_entry.resize(200, 20)
         username_h_box.addWidget(self.name_entry)
         
         Fname_h_box=QHBoxLayout()
         name_label = QLabel("First Name:", self)
         Fname_h_box.addWidget(name_label)
         
         self.name_entry2 = QLineEdit(self)
         
         self.name_entry2.resize(200, 20)
         Fname_h_box.addWidget(self.name_entry2)
         
         lname_h_box=QHBoxLayout()
         
         name_label1 = QLabel("last Name:", self)
         name_label1.move(50, 210)
         self.name_entry1 = QLineEdit(self)
         self.name_entry1.move(130, 210)
         self.name_entry1.resize(200, 20)
         lname_h_box.addWidget(name_label1)
         lname_h_box.addWidget(self.name_entry1)
         
         
         pw_h_box=QHBoxLayout()
         
         pw=QLabel("password",self)
         
         self.pswd_entry = QLineEdit(self)
         
         self.pswd_entry.resize(200, 20)
         
         pw_h_box.addWidget(pw)
         pw_h_box.addWidget(self.pswd_entry)
         
         pwc_h_box=QHBoxLayout()
         
         
         confirm_label = QLabel("confirm:", self)
         confirm_label.move(50, 270)
         self.confirm_entry = QLineEdit(self)
         
         self.confirm_entry.resize(200, 20)
         
         pwc_h_box.addWidget(confirm_label)
         pwc_h_box.addWidget(self.confirm_entry)
         
         gender_h_box=QHBoxLayout()
         name=QLabel("gender",self)
         name.move(100,300)
         self.gender = QLineEdit(self)
         
         self.gender.resize(200, 20)
         
         gender_h_box.addWidget(name)
         gender_h_box.addWidget(self.gender)
         
         age_h_box=QHBoxLayout()
         age=QLabel("age",self)
         age.move(100,300)
         self.age1 = QLineEdit(self)
         
         self.age1.resize(200, 20)
         age_h_box.addWidget(age)
         age_h_box.addWidget(self.age1)
         
         v_box=QVBoxLayout()
         v_box.addLayout(title_h_box)
         v_box.addLayout(username_h_box)
         v_box.addLayout(Fname_h_box)
         v_box.addLayout(lname_h_box)
         v_box.addLayout(pw_h_box)
         v_box.addLayout(pwc_h_box)
         v_box.addLayout(gender_h_box)
         v_box.addLayout(age_h_box)
         
         
         
         
         
         
         
         sign_up_button = QPushButton("sign up", self)
         
         sign_up_button.resize(200, 40)
         sign_up_button.clicked.connect(self.confirmSignUp)
         
         v_box.addWidget(sign_up_button)
         
         self.setLayout(v_box)
         
         
         
    def confirmSignUp(self):
        """
        When  user presses sign up, check if the passwords match.
        If they match, then save username and password text to users.txt.
        """
        pswd_text = self.pswd_entry.text()
        confirm_text = self.confirm_entry.text()
        if pswd_text != confirm_text:
            # Display messagebox if passwords don't match
            QMessageBox.warning(self, "Error Message","The passwords you entered do not match. Please try again.", QMessageBox.Close,QMessageBox.Close)
        else:
            mycur.execute("select max(customerid) from customer")
            a=mycur.fetchone()
            if a[0]:
                
                b=a[0]
                
            else:
                b=0
                
            
        
            user1=customer(self.name_entry2.text(),self.name_entry1.text(),self.gender.text().capitalize(),int(self.age1.text()),self.name_entry.text(),self.pswd_entry.text(),int(b)+1)
            mycur.execute("insert into customer values({},'{}','{}','{}',{},'{}','{}')".format((int(b)+1),user1.name,user1.surname,user1.gender,user1.age,user1.username,user1.password))
            QMessageBox.warning(self, "Success Message","Account Created Succesfully", QMessageBox.Close,QMessageBox.Close)
            mydb.commit()
                
             
                 
                 
                 
                 
                 
if __name__ == '__main__':
     
     app = QApplication(sys.argv)
     window = CreateNewUser()
     sys.exit(app.exec_())    



             