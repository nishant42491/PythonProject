
import pandas as pd
import os
import mysql.connector as conn
mydb = conn.connect(host="localhost",user="root",password="root",database="shop")
mycur=mydb.cursor(buffered=True)



import sys
from PyQt5.QtWidgets import (QApplication,QMessageBox,QHBoxLayout,QVBoxLayout, QWidget,QCheckBox, QLabel, QLineEdit, QPushButton)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from Registration import CreateNewUser
from Homepage import HomePageView
from Catalogue import CatalaogueView


class LoginUi(QWidget): # Inherits QWidget
     def __init__(self): # Constructor
         super().__init__() # Initializer which calls constructor for QWidget
         self.initializeUI() # Call function used to set up window
         


     def initializeUI(self):
         """
         Initialize the window and display its contents to the screen
         """
         self.setGeometry(100, 100, 400, 200)
         self.setWindowTitle('Customer Management Shop')
         self.loginUserInterface()
         
         self.show()
     
        
    
     def loginUserInterface(self):
         """
         Create the login GUI.
         """
         login_label = QLabel(self)
         login_label.setText("login")
         login_label.move(180, 10)
         login_label.setFont(QFont('Arial', 20))
         # Username and password labels and line edit widgets
         name_label = QLabel("username:", self)
         name_label.move(30, 60)
         self.name_entry = QLineEdit(self)
         self.name_entry.move(110, 60)
         self.name_entry.resize(220, 20)
         password_label = QLabel("password:", self)
         password_label.move(30, 90)
         self.password_entry = QLineEdit(self)
         self.password_entry.move(110, 90)
         self.password_entry.resize(220, 20)
         # Sign in push button
         sign_in_button = QPushButton('login', self)
         sign_in_button.move(100, 140)
         sign_in_button.resize(200, 40)
         sign_in_button.clicked.connect(self.clickLogin)
         # Display show password checkbox
         show_pswd_cb = QCheckBox("show password", self)
         show_pswd_cb.move(110, 115)
         show_pswd_cb.stateChanged.connect(self.showPassword)
         show_pswd_cb.toggle()
         show_pswd_cb.setChecked(False)
         # Display sign up label and push button
         not_a_member = QLabel("not a member?", self)
         not_a_member.move(70, 200)
         sign_up = QPushButton("sign up", self)
         sign_up.move(160, 195)
         sign_up.clicked.connect(self.createNewUser)
         
         
     def clickLogin(self):
         """
         When user clicks sign in button, check if username and password 
        match any existing profiles in users.txt.
         If they exist, display messagebox and close program.
         If they don't, display error messagebox.
         """
         
         username = self.name_entry.text()
         password = self.password_entry.text()
         
         pwd={}
         mycur.execute("select * from customer")
         a=mycur.fetchall()
        
         for x in a:
            pwd[x[1]]=[x[0],x[-2],x[-1]]
         for x,y in pwd.items():
             
             if y[-2]==username and y[-1]==password:
                 
                 
                 
                 
                 
                 QMessageBox.information(self, "Login Successful!", "Login Successful!", QMessageBox.Ok, QMessageBox.Ok)
                 
                  # close program
                 
                 a=[x,y[0]]
                 self.homepage(a[0],a[1])
                
                 
                 
                 break
                    
    
     def homepage(self,cname,cid):
         self.np=HomePageView(cname,cid)
         self.np.show()
         
        
         
         
     
     
     
     
     def showPassword(self, state):
         '''
         If checkbox is enabled, view password.
         Else, mask password so others cannot see it.
         '''
         if state == Qt.Checked:
             self.password_entry.setEchoMode(QLineEdit.Normal)
         else:
             self.password_entry.setEchoMode(QLineEdit.Password)   
     
     
     
     def createNewUser(self):
         """
         When the sign up button is clicked, open
         a new window and allow the user to create a new account.
         """
         self.create_new_user_dialog = CreateNewUser()
         self.create_new_user_dialog.show()
     
     def closeEvent(self, event):
         """
         Display a QMessageBox when asking the user if they want to quit the 
        program.
         """
         # Set up message box
         quit_msg = QMessageBox.question(self, "Quit Application?",
         "Are you sure you want to Quit?", QMessageBox.No | QMessageBox.Yes,
         QMessageBox.Yes)
         if quit_msg == QMessageBox.Yes:
             event.accept() # accept the event and close the application
         else:
             event.ignore() # ignore the close event
             
     
     
         
         
         
         
     
         
         
if __name__ == '__main__':
     mycur.execute("delete from orders where quantity=0")
     mydb.commit()
     app = QApplication(sys.argv)
     window=LoginUi()
     sys.exit(app.exec_())