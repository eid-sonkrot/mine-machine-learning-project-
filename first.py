# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 18:07:41 2023

@author: eid
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from tkinter import *
import joblib
def run1():
    try :
      p1 = float(e1.get())
      p2 = float(e2.get())
      result=model.predict([[p1,p2]])
      Label(main,text='sum is =').grid(row=4)
      Label(main,text=float(result[0])).grid(row=5)
    except ValueError:
        print("error")
     
     
data=pd.read_csv("add.csv")
x=data[['x','y']]
y=data['sum']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=42)
model=LinearRegression()
model.fit(x_train, y_train)
joblib.dump(model, 'sumtwovalue')
main=Tk()
main.title('Add two number')
label=Label(main,text='add two number',bg='black',fg='white').grid(row=0,columnspan=2)
Label(main,text='entier first number').grid(row=1)
Label(main,text='entire second number').grid(row=2)
e1=Entry(main)
e2=Entry(main)
e1.grid(row=1,column=1)
e2.grid(row=2,column=1)
Button(main,text='result',command=run1).grid(row=3)
mainloop()





