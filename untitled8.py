# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 15:29:56 2022

@author: Dell
"""

from tkinter import*
from PIL import ImageTk,Image
from tkinter import filedialog

import os
import webbrowser
import tkinter.messagebox as msg
root = Tk()
root.minsize(700,700)
root.maxsize(700,700)

open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
run_img = ImageTk.PhotoImage(Image.open("run1.png"))

label_file_name = Label(root,text = "File name")
label_file_name.place(relx = 0.3 , rely = 0.03 , anchor = CENTER)
input_file_name = Entry(root )
input_file_name.place(relx = 0.46 , rely = 0.03 , anchor = CENTER)
text_area = Text(root,width = 80 , height = 35 , bg = "gray15" , fg = "white")
text_area.place(relx = 0.5 , rely = 0.55 , anchor = CENTER)
name = ""
def openfile():
    global name
    text_area.delete(1.0,END)
    input_file_name.delete(0 , END)
    html_file = filedialog.askopenfilename(title = "File Dialog" , filetypes = (("html files" , "*.html"),))
    name = os.path.basename(html_file)
    formatted_name = name.split(".")[0]
    input_file_name.insert(0 , formatted_name)
    root.title(formatted_name)
    html_file = open(name , "r")
    paragraph = html_file.read()
    text_area.insert(1.0 , paragraph)
    html_file.close()

  
    
def save_file():
    file_name = input_file_name.get()
    file = open(file_name + ".html" , "w")
    data = text_area.get(1.0 , END)
    file.write(data)
    text_area.delete(1.0 , END)
    input_file_name.delete(0 , END)
    msg.showinfo("update" , "Success")

def run_file():
   global name
   webbrowser.open(name)

btn_open = Button(root , image = open_img , command = openfile)
btn_open.place(relx = 0.05 , rely = 0.03 , anchor = CENTER)
btn_save = Button(root , image = save_img , command = save_file)
btn_save.place(relx = 0.11 , rely = 0.03 , anchor = CENTER)
btn_run = Button(root , image = run_img , command = run_file)
btn_run.place(relx = 0.17 , rely = 0.03 , anchor = CENTER)
root.mainloop()