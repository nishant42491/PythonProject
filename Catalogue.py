# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 18:30:01 2021

@author: nishant
"""

import sys
from PyQt5.QtWidgets import (QTableWidget,QMainWindow,QApplication, QWidget, QMessageBox, QPushButton, QLabel, QLineEdit,QHBoxLayout,QVBoxLayout,QTableWidget,QTableWidgetItem)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QRect
from table1 import Ui_MainWindow
import pandas as pd
import os
import mysql.connector as conn
mydb = conn.connect(host="localhost",user="root",password="root",database="shop")
mycur=mydb.cursor()

class CatalaogueView(QMainWindow):
    def __init__(self):
        super(CatalaogueView, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        
        
        

    
        
        
                
           
            
           
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    w=CatalaogueView()
    w.show()
    
    sys.exit(app.exec_())
        