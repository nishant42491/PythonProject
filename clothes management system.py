# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 13:59:32 2021

@author: nishant
"""
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

def reg(count1):
    
    print('''welcome to the registartion window''')
    user1=customer(input("enter name: ").strip(),input("enter surname: ").strip(),input("enter gender: ").strip().capitalize(),int(input("Enter Age: ").strip()),input("enter username: ").strip(),input("enter Password: ").strip(),count1)
    mycur.execute("insert into customer values({},'{}','{}','{}',{},'{}','{}')".format(count1,user1.name,user1.surname,user1.gender,user1.age,user1.username,user1.password))
    print ("user created succesfully")
    mydb.commit()

def login():
     
        eu=input("enter username: ")
        ep=input("enter password: ")
        pwd={}
        mycur.execute("select * from customer")
        a=mycur.fetchall()
        
        for x in a:
            pwd[x[1]]=[x[0],x[-2],x[-1]]
        for x,y in pwd.items():
            if y[-2]==eu and y[-1]==ep:
                a=[1,x,y[0]]
                return a
                break
                
        return[0,8]    

def view1():
    mycur.execute("select productname as product,price as price,stock as stock from product")
    x=mycur.fetchall()
        
       
    df=pd.DataFrame(x)
    df.columns=['product name','price','stock']
    print("\n")
    print(df)
    print("\n")


def cart(idnm):
    mycur.execute("select cname,productname,quantity,price from orders inner join product on orders.pid=product.productid where customerid = {}".format(idnm))
    a=mycur.fetchall()
    if len(a)==0:
        print("CART EMPTY!!!! ADD Products")
    
    else:
        df=pd.DataFrame(a)
    
        df.columns=['customer name','product name','quantity','price per item']
        print(df)
        return a
    
def addtocart(idnm,cname):
    print('''warning existing items from cart will be deleted''')
    print('''do you want to continue Y for yes N for no''')
    an=input("enter here: ").capitalize()
    if an == 'N':
        pass
    else:
        print('''items wiped out''')
        mycur.execute("delete from orders")
        pid=int(input("enter product id: "))
        q=int(input("enter quantity: "))
        mycur.execute("insert into orders values({},'{}',{},{})".format(idnm,cname,pid,q))
        mydb.commit()
        print('''products added!!!''')
        
def checkout(idnm):
    mtq=cart(idnm)
    d={}
    for a in mtq:
        d[a[1]]=[a[2],a[3]]
        
    sum1=0
    for x,y in d.items():
        sum1+=(y[0]*y[1])
    print("your total is ",sum1) 
    print("do you want to proceed Y for yes N for no")
    ip=input("enter here: ").capitalize()
    if ip=='Y':
        l={}
        mycur.execute("select quantity,price,stock,pid from orders inner join product on orders.pid=product.productid where customerid = {}".format(idnm))
        nm=mycur.fetchall()
        for te in nm:
            l[str(te[0])]=[te[1],te[2],te[3]]
        for x,y in l.items():
            left=y[1]-int(x)
            mycur.execute("update product set stock={} where productid={}".format(left,y[2]))
        print("Items are purchased succesfully")
        print("Thank you")
        
        
    
        
    
    
        
        
        
        
op=1
mycur.execute("select max(customerid) from customer ")
count1=mycur.fetchone()[0]+1
if count1==None:
    count1=1
else:
    pass
    

while op == 1:
            
            print("press 1 to register or 2 to login press 3 to quit: ")
            a= int(input())
            if a==1:
                reg(count1)
                count1+=1
                
           
            elif a == 2:
              m=login()
              if m[0]==1:
                  op = 0
              else:
                  print("wrong password or username ")
            
            
           
            
            
            else:
                print('''continue Y or N''')
                if input().strip().capitalize()=='N':
                    os._exit(0)
        
        
        
print('\n welcome user {} \n'.format(m[1]) )
while 1:
        
    
    print('''\npress 1 to see catalogue\n2 to see cart\n3 add products to cart\n4 for chack-out\n5 to exit\n''')
            
    a=int(input('enter here: '))  
    if a == 1:
        view1()
    elif a == 2:
        cart(m[-1])
    elif a == 3:
        addtocart(m[-1],m[1])
    
    elif a==4:
        checkout(m[-1])
        
        
        
    elif a == 5:
        print("thank you for using CMS!!!!")
        os._exit(0)
        
       