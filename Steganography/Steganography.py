
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk 
import os
from stegano import lsb 

root = Tk()
root.title("Steganographic Forensic Tool")
root.geometry("700x500+250+180")
root.configure(bg="#2f4155")

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir = os.getcwd(),
                                          title = 'Select Image File',
                                          filetype = (("PNG file" , "*.png"),
                                                      ("JPG File" , "*.jpg") , ("All file" , '*.txt')))
    global img ;img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image = img , width = 250 , height = 250)
    lbl.image = img

def Hide():
    global secret 
    message = text_1.get(1.0 , END)
    secret =lsb.hide(str(filename) , message)

def Show():
    clear_message = lsb.reveal(filename)
    text_1.delete(1.0 , END)
    text_1.insert(END , clear_message)

def save():

    try:
        if img is None:   
            print("")
            return
    except NameError:
        print('No image Loaded')
        return
    
    
    options = {
        'title' : 'Save file as',
        'defaultextension' : '.png',
        'filetypes' : [('PNG files' , '*.png') , ('JPEG files' , '*.jpg;*.jpeg')]
    }

    file_path = filedialog.asksaveasfilename(**options)
    if file_path:
        if secret:
            secret.save(file_path)
            print(f'File saved as {file_path}')
        else:
            print('No hiiden message to save')
        
    else:
        print('Operation Failed or cancelled')

    #secret.save("Hidden.png")

#importing and setting icon
image_icon = PhotoImage(file = "logo.jpg")
root.iconphoto(False , image_icon);

logo = PhotoImage(file="logo.png")
Label(root , image=logo , bg = "#2f4155").place(x = 10 , y = 0)

Label(root , text = "CYBER SCIENCE" , bg = '#2d4155' , fg = 'white' , font="arial 25 bold").place(x = 100 , y = 20)

frame_1 = Frame(root , bd=3 , bg = 'black' , width = 340 , height = 280 , relief = GROOVE)
frame_1.place(x = 10 , y = 80)

lbl = Label(frame_1,bg='black')
lbl.place(x = 40 , y = 10)

frame_2 = Frame(root , bd=3 , width=340 , height = 280 , bg = 'white' , relief = GROOVE)
frame_2.place(x = 350 , y = 80) 

text_1 = Text(frame_2 , font = 'Robote 20' , bg = 'white' , fg = 'black' , relief = GROOVE , wrap = WORD)
text_1.place(x = 0 , y = 0 , width = 320 , height = 295)

Scrollbar_1 = Scrollbar(frame_2)
Scrollbar_1.place(x = 320 , y = 0 , height = 300)

Scrollbar_1.configure(command = text_1.yview)
text_1.configure(yscrollcommand = Scrollbar_1.set)

frame_3 = Frame(root , bd = 3 , bg = '#2f4155' , width = 330 , height = 100 , relief = GROOVE)
frame_3.place(x = 10 , y = 370)

Button(frame_3 , text = "Open Image" , width = 10 , height = 2 , font = "arial 14 bold" , command = showimage).place(x = 20 , y = 30)
Button(frame_3 , text = "Save Image" , width = 10 , height = 2 , font = "arial 14 bold" , command = save).place(x = 180 , y = 30)
Label(frame_3 , text = "Picture , Image , Photo File" , bg = "#2f4155" , fg = 'yellow').place(x = 20 , y = 5)

frame_4 = Frame(root , bd = 3 , bg = '#2f4155' , width = 330 , height = 100 , relief = GROOVE)
frame_4.place(x = 360 , y = 370)

Button(frame_4 , text = "Hide Data" , width = 10 , height = 2 , font = "arial 14 bold" , command = Hide).place(x = 20 , y = 30)
Button(frame_4 , text = "Show Data" , width = 10 , height = 2 , font = "arial 14 bold" , command = Show).place(x = 180 , y = 30)
Label(frame_4 , text = "Picture , Image , Photo File" , bg = "#2f4155" , fg = 'yellow').place(x = 20 , y = 5)

root.mainloop() 
