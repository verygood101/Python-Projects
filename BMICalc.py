from cProfile import label
from cgitb import text
from importlib.metadata import entry_points
import tkinter
from math import *
from tkinter import *
from tkinter import messagebox

usrWindow = Tk()

# function that calculates BMI
# gets the usrHeight and usrWeight as integers
def bmiCalculate():
    usrHeight = float(entHeight.get())
    usrWeight = float(entWeight.get())

    usrBMI = usrWeight / (usrHeight/100)**2
    
    if usrBMI <= 18.4:
        usrComments = "You are considered underweight"
    elif usrBMI <= 24.9:
        usrComments = "You are considered healthy"
    elif usrBMI <= 29.9:
        usrComments = "You are considered overweight"
    elif usrBMI <= 39.9:
        usrComments = "You are considered obese" 
    else:
        usrComments = "You are severely obese"  

    messagebox.showinfo("BMI Calc",f"Your BMI is {round(usrBMI,1)}. {usrComments}")

#resizes window and sets the window title.
usrWindow.title("BMI Calculator")
usrWindow.geometry("400x300")

# creates label and packs it into the window. 
lblTitle = Label(usrWindow, text = "BMI Calculator")
lblTitle.pack()

# creates entry field and label for user's height.
lblHeight = Label(usrWindow, text = "Height")
lblHeight.pack()
entHeight = Entry(usrWindow)
entHeight.pack()

# creates entry field and label for user's weight.
lblWeight = Label(usrWindow, text = "Weight")
lblWeight.pack()
entWeight = Entry(usrWindow)
entWeight.pack()

# creates button that calculates the BMI.
btnCalculate = Button(usrWindow, text = "Calculate", command = bmiCalculate)
btnCalculate.pack()


usrWindow.mainloop()
