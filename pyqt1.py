# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 18:23:29 2021

@author: nishant
"""

import sys,os.path
from PyQt5.QtWidgets import QApplication,QLabel,QWidget
from PyQt5.QtGui import QFont,QPixmap

class UserProfile(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initializeUI()
    
        
    def initializeUI(self):
        self.setGeometry(50,50,250,400)
        self.setWindowTitle("User Profile")
        self.displayImages()
        self.displayUserInfo()
        self.show()
    
        
    def displayImages(self):
        background_image="images/skyblue.png"
        profile_image="images/skyblue.png"
        try:
            with open(background_image):
                background=QLabel(self)
                pixmap=QPixmap(background_image)
                background.setPixmap(pixmap)
        except:
            print("Image not found")
        
        
        try:
            with open(profile_image):
                userimage=QLabel(self)
                pixmap=QPixmap(profile_image)
                userimage.setPixman(pixmap)
        except:
            print("image not found")
            
        
    def displayUserInfo(self):
        user_name=QLabel(self)
        user_name.setText("Nishant Rajadhyaksha")
        user_name.move(85,140)
        user_name.setFont(QFont('Arial',20))
        
if __name__=='__main__':
     app=QApplication(sys.argv)
     window=UserProfile()
     sys.exit(app.exec_())
     
     
        