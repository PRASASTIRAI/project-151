# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 21:32:11 2021

@author: hp
"""

from tkinter import*

root=Tk()
root.title("PROFIT SHOWING APP")
root.geometry("400x400")

month_label=Label(root)
profit_label=Label(root)
profit_gained_maximum=Label(root)
profit_gained_minimum=Label(root)


month = ("january","february","march","april","may","june","july","august","september","october","november","december")

profit = (12,20,30,40,100,10,3,9,0,200,300,800)

month_label["text"] = "january , February , March , April , May , June , July , August , September , October , November , December"
month_label.place(relx=0.4,rely=0.4,anchor=CENTER)
profit_label["text"]="12,20,30,40,100,10,3,9,0,200,300,800"
profit_label.place(relx=0.5,rely=0.4,anchor=CENTER)
max_profit= max(profit)
max_profit_index = profit.index(max_profit)


max_profit_month = month[max_profit_index]
profit_gained_maximum=Label("the maximum profit : " + str(max_profit)+" were recording in the month of : "+ str(max_profit_month))

min_profit=min(profit)
min_profit_index= profit.index(min_profit)
print(min_profit_index)

min_profit_month = month[min_profit_index]
profit_gained_minimum=Label("the minmum profit : " + str(min_profit)+" were recording in the month of : "+ str(min_profit_month))

root.mainloop()