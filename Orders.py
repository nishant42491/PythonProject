# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 11:58:38 2021

@author: nishant
"""

import sys
from PyQt5.QtWidgets import (QTableWidget,QMainWindow,QApplication, QWidget, QMessageBox, QPushButton, QLabel, QLineEdit,QHBoxLayout,QVBoxLayout,QTableWidget,QTableWidgetItem)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QRect
from order1 import Ui_MainWindow
import pandas as pd
import os
import mysql.connector as conn
mydb = conn.connect(host="localhost",user="root",password="root",database="shop")
mycur=mydb.cursor()

class OrdersView(QMainWindow):
    def __init__(self,cname,cid):
        super(OrdersView, self).__init__()
        self.cname=cname
        self.cid=cid

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow(self.cname,self.cid)
        self.ui.setupUi(self)
        
        
        
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    w=OrdersView("kaka", 21)
    w.show()
    
    sys.exit(app.exec_())        