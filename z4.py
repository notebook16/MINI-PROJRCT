#Import the required library
from tkinter import*
from PIL import Image, ImageTk

win = Tk()

# Define the geometry of the window

win.geometry("800x700")

def khtm():
    win.destroy() 

def lost():
    frame1 = Frame(win, width=600, height=400)
    frame1.pack()
    frame1.place(anchor='center', relx=0.5, rely=0.5)
    img2 = ImageTk.PhotoImage(Image.open("lost.png"))
    label = Label(frame1, image=img2, compound='center')
    label.pack()
    label.image=img2
    

def winer():
    frame1 = Frame(win, width=600, height=400)
    frame1.pack()
    frame1.place(anchor='center', relx=0.5, rely=0.5)
    img2 = ImageTk.PhotoImage(Image.open("win.png"))
    label = Label(frame1, image=img2, compound='center')
    label.pack()
    b2 = Button(win, text= "exit" , bg = "yellow", command= khtm)
    b2.place(x=330, y=600)
    label.image=img2

def second_riddle():
    frame1 = Frame(win, width=600, height=400)
    frame1.pack()
    frame1.place(anchor='center', relx=0.5, rely=0.5)
    img2 = ImageTk.PhotoImage(Image.open("second riddle.png"))
    label = Label(frame1, image=img2, compound='center')
    label.pack()
    b2 = Button(win, text= "word",command=lost)
    b3 = Button(win, text= "language",command=winer)
    b4 = Button(win, text= "communication",command=lost)
    b5 = Button(win, text= "social",command=lost)
    b2.place(x=200, y=430)
    b3.place(x=300, y=430)
    b4.place(x=400, y=430)
    b5.place(x=550, y=430)
    label.image=img2



def first_riddle():
    frame1 = Frame(win, width=600, height=400)
    frame1.pack()
    frame1.place(anchor='center', relx=0.5, rely=0.5)
    img2 = ImageTk.PhotoImage(Image.open("first riddle.png"))
    label = Label(frame1, image=img2, compound='center')
    label.pack()
    b2 = Button(win, text= "BCDAE",command=second_riddle)
    b3 = Button(win, text= "CABDE",command=winer)
    b4 = Button(win, text= "ABCDE",command=second_riddle)
    b5 = Button(win, text= "DCAB",command=second_riddle)
    b2.place(x=250, y=350)
    b3.place(x=350, y=350)
    b4.place(x=450, y=350)
    b5.place(x=550, y=350)
    label.image=img2

    


def riddle_intro():
    frame1 = Frame(win, width=600, height=400)
    frame1.pack()
    frame1.place(anchor='center', relx=0.5, rely=0.5)
    img2 = ImageTk.PhotoImage(Image.open("riddle intro.png"))
    label = Label(frame1, image=img2, compound='center')
    label.pack()
    b2 = Button(win, text= "continue" , bg = "yellow", command= first_riddle)
    b2.place(x=500, y=400)
    label.image=img2

    


def reaching_charlie():
    frame1 = Frame(win, width=600, height=400)
    frame1.pack()
    frame1.place(anchor='center', relx=0.5, rely=0.5)
    img2 = ImageTk.PhotoImage(Image.open("meet.png"))
    label = Label(frame1, image=img2, compound='center')
    label.pack()
    b2 = Button(win, text= "coninue" , bg = "yellow", command= riddle_intro)
    b2.place(x=100, y=400)
    label.image=img2

def first_r():
    frame1 = Frame(win, width=600, height=400)
    frame1.pack()
    frame1.place(anchor='center', relx=0.5, rely=0.5)
    img2 = ImageTk.PhotoImage(Image.open("rec ch.png"))
    label = Label(frame1, image=img2, compound='center')
    label.pack()
    b2 = Button(win, text= "1995" )
    b3 = Button(win, text= "1991" )
    b4 = Button(win, text= "2000", command=reaching_charlie)
    b5 = Button(win, text= "2002" )
    b2.place(x=250, y=350)
    b3.place(x=350, y=350)
    b4.place(x=450, y=350)
    b5.place(x=550, y=350)
    label.image=img2



def com_intro():
    frame1 = Frame(win, width=600, height=400)
    frame1.pack()
    frame1.place(anchor='center', relx=0.5, rely=0.5)
    img2 = ImageTk.PhotoImage(Image.open("computer intro.png"))
    label = Label(frame1, image=img2, compound='center')
    label.pack()
    b2 = Button(win, text= "yes" , command= first_r)
    b2.place(x=500, y=400)
    label.image=img2



def find_computer():
    frame1 = Frame(win, width=600, height=400)
    frame1.pack()
    frame1.place(anchor='center', relx=0.5, rely=0.5)
    img2 = ImageTk.PhotoImage(Image.open("finds computer.png"))
    label = Label(frame1, image=img2, compound='center')
    label.pack()
    b2 = Button(win, text= "continue" ,  bg = "yellow",command= com_intro)
    b2.place(x=500, y=400)
    label.image=img2





def enter_room():
    frame1 = Frame(win, width=600, height=400)
    frame1.pack()
    frame1.place(anchor='center', relx=0.5, rely=0.5)
    img2 = ImageTk.PhotoImage(Image.open("open rooms.png"))
    label = Label(frame1, image=img2, compound='center')
    label.pack()
    b2 = Button(win, text= "continue" , bg = "yellow", command= find_computer)
    b2.place(x=500, y=400)
    label.image=img2




def fourth_level():
    frame1 = Frame(win, width=600, height=400)
    frame1.pack()
    frame1.place(anchor='center', relx=0.5, rely=0.5)
    img2 = ImageTk.PhotoImage(Image.open("fourth.png"))
    label = Label(frame1, image=img2, compound='center')
    label.pack()
    b2 = Button(win, text= "auditorium" )
    b3 = Button(win, text= "ground" )
    b4 = Button(win, text= "store room", command=enter_room )
    b5 = Button(win, text= "classroom" )
    b2.place(x=400, y=520)
    b3.place(x=500, y=520)
    b4.place(x=600, y=520)
    b5.place(x=700, y=520)
    label.image=img2


def third_level():
    frame1 = Frame(win, width=600, height=400)
    frame1.pack()
    frame1.place(anchor='center', relx=0.5, rely=0.5)
    img2 = ImageTk.PhotoImage(Image.open("third.png"))
    label = Label(frame1, image=img2, compound='center')
    label.pack()
    b2 = Button(win, text= "mall" )
    b3 = Button(win, text= "farm" )
    b4 = Button(win, text= "school", command=fourth_level )
    b5 = Button(win, text= "stadium" )
    b2.place(x=400, y=400)
    b3.place(x=500, y=400)
    b4.place(x=600, y=400)
    b5.place(x=700, y=400)
    label.image=img2

def second_level():
    frame1 = Frame(win, width=600, height=400)
    frame1.pack()
    frame1.place(anchor='center', relx=0.5, rely=0.5)
    img2 = ImageTk.PhotoImage(Image.open("second2.png"))
    label = Label(frame1, image=img2, compound='center')
    label.pack()
    b2 = Button(win, text= "golden street" )
    b3 = Button(win, text= "lamp street" , command= third_level)
    b4 = Button(win, text= "round street" )
    b5 = Button(win, text= "winter street" )
    b2.place(x=400, y=400)
    b3.place(x=500, y=400)
    b4.place(x=600, y=400)
    b5.place(x=700, y=400)
    label.image=img2

def first_level():
    frame1 = Frame(win, width=600, height=400)
    frame1.pack()
    frame1.place(anchor='center', relx=0.5, rely=0.5)
    img2 = ImageTk.PhotoImage(Image.open("first.png"))
    label = Label(frame1, image=img2, compound='center')
    label.pack()
    b2 = Button(win, text= "coffee house" , command= second_level)
    b3 = Button(win, text= "house" )
    b4 = Button(win, text= "hospital")
    b5 = Button(win, text= "park" )
    b2.place(x=350, y=400)
    b3.place(x=500, y=400)
    b4.place(x=600, y=400)
    b5.place(x=700, y=400)
    label.image=img2



def intro():
    frame1 = Frame(win, width=600, height=400)
    frame1.pack()
    frame1.place(anchor='center', relx=0.5, rely=0.5)
    img2 = ImageTk.PhotoImage(Image.open("800x800.1.png"))
    label = Label(frame1, text= "enter the place", image=img2, compound='center')
    label.pack()
    b2 = Button(win, text= "yes" , font='bold',bg= 'yellow', height=5,width=8, command= first_level)
    b2.place(x=350, y=400)
    label.image=img2
     

def start():
    frame1 = Frame(win, width=800, height=800)
    frame1.pack()
    frame1.place(anchor='center', relx=0.5, rely=0.5)
    img2 = ImageTk.PhotoImage(Image.open("second.png"))
    label = Label(frame1, image=img2, compound='center')
    label.pack()
    b2 = Button(win, text= "yes" , width = 5 , height = 5, bg =  "#878700",command= intro)
    b3 = Button(win, text= "no" ,width = 5 , height = 5 , bg ="#D7D75F" ,command= khtm)
    b2.place(x=350, y=600)
    b3.place(x=400,y=600)
    label.image=img2



frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("VWqaoBhS2y7mBm7ss3bUTT.jpg"))

# Create a Label Widget to display the text or Image
label = Label(frame,image = img,compound= 'center')
label.pack()

btn = Button(win, text = 'start game!', fg = "red" ,  bg = "#5FFFFF", height = 8 , width=15, command = start,)
 
# Set the position of button to coordinate (100, 20)
btn.place(x=350, y=300)
 


win.mainloop()