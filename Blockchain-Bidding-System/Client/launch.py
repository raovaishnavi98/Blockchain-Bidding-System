from tkinter import *
#import matplotlib
#matplotlib.use('Agg')
import subprocess
import additemform

top = Tk()
top.geometry("750x500")

def add_item():
   start()


title_label = Label(top, text="WELCOME TO BIDDING PLATFORM", font=("Verdana, italic, bold", 20), padx="25px", pady="25px").grid(row=0, column=0, columnspan=9)

add_item_btn = Button(top, text = "ADD ITEM", command = additemform.start, relief=RIDGE, bg="#ff8533", activebackground="#ff8533", fg="white", font=("Times New Roman", 18), borderwidth="1", padx="10px").grid(row=1, column=0, rowspan=2)

show_item_btn = Button(top, text = "SHOW ITEM", command = "", relief=RIDGE, bg="#79ff4d", activebackground="#79ff4d", fg="white", font=("Times New Roman", 18), borderwidth="1", padx="10px").grid(row=1, column=2, rowspan=2)

add_bid_btn = Button(top, text = "ADD BID", command = "", relief=RIDGE, bg="#80ffd4", activebackground="#80ffd4", fg="white", font=("Times New Roman", 18), borderwidth="1", padx="10px").grid(row=1, column=4, rowspan=2)

show_bid_btn = Button(top, text = "SHOW BID", command = "", relief=RIDGE, bg="#d580ff",activebackground="#d580ff", fg="white", font=("Times New Roman", 18), borderwidth="1", padx="10px").grid(row=1, column=6, rowspan=2)



top.mainloop()
