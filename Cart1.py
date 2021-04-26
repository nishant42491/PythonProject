# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 13:00:22 2021

@author: nishant
"""

import sys
from PyQt5.QtWidgets import (QTableWidget,QMainWindow,QApplication, QWidget, QMessageBox, QPushButton, QLabel, QLineEdit,QHBoxLayout,QVBoxLayout,QTableWidget,QTableWidgetItem)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QRect
from cart import Ui_MainWindow

import pandas as pd
import os
import mysql.connector as conn
mydb = conn.connect(host="localhost",user="root",password="root",database="shop")
mycur=mydb.cursor()


class CartView(QMainWindow):
    def __init__(self,cname,cid):
        super(CartView,self).__init__()
        self.cname=cname
        self.cid=cid

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow(self.cname,self.cid)
        self.ui.setupUi(self)
        
        