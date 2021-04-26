# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 11:36:02 2021

@author: nishant
"""

import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow, QWidget, QMessageBox, QPushButton, QLabel, QLineEdit,QHBoxLayout,QVBoxLayout)
from PyQt5.QtGui import QFont, QPixmap
from Catalogue import CatalaogueView
from Orders import OrdersView
from Cart1 import CartView



class HomePageView(QWidget):
    
    def __init__(self,cname,cid):
        
        super().__init__()
        self.cname=cname
        self.cid=cid
        self.initializeUI()
        
        
    def initializeUI(self):
         """
         Initialize the window and display its contents to the screen
         """
         self.setGeometry(100, 100, 400, 400)
         self.setWindowTitle('Homepage')
         self.Welcome()
         self.show()    
         

    def Welcome(self):
        title_h_box=QHBoxLayout()
        r=QLabel("welcome User {}".format(self.cname),self)
        title_h_box.addWidget(r)
        button_h_box=QHBoxLayout()
        catalogue=QPushButton("Catalogue",self)
        catalogue.clicked.connect(self.catalogue)
        order=QPushButton("Order")
        order.clicked.connect(self.order)
        cart=QPushButton("Cart")
        cart.clicked.connect(self.cart)
        button_h_box.addWidget(catalogue)
        button_h_box.addWidget(order)
        button_h_box.addWidget(cart)
        
        v_box=QVBoxLayout()
        v_box.addLayout(title_h_box)
        v_box.addLayout(button_h_box)
        self.setLayout(v_box)
        

    def catalogue(self):
       
       self.kd=CatalaogueView()
       self.kd.show()
        
        
        
        


    def cart(self):
        self.md=CartView(self.cname,self.cid)
        self.md.show()
        
    
    
    def order(self):
        self.hf=OrdersView(self.cname,self.cid)
        self.hf.show()
        
        
        
        
        
        