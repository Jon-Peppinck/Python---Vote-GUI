# Voting GUI - Jon Peppinck

from tkinter import *
from tkinter import ttk

#The three functions below get the initial value of votes of 0 and adds one to it every
#time the function is executed via clicking/touching the option the user wishes to vote for

def add_One_Elif_Farm():
	x = int(value_EF.get())
	value_EF.set(x+1)

def add_One_For_Loop_Range():
	y = int(value_FLR.get())
	value_FLR.set(y+1)

def add_One_List_Append_Stud():
	z = int(value_LAS.get())
	value_LAS.set(z+1)

#Creates window and title for GUI

root = Tk()
root.title("Pythonville Voting System")

#Configures rows and columns to resize proportionally 

root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight = 1)
root.columnconfigure(2, weight = 1)
root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 1)
root.rowconfigure(2, weight = 1)

#Values from the functions are converted into string variables so the labels can display text variables

value_EF = StringVar()
value_FLR = StringVar()
value_LAS = StringVar()

#Initial value of each function is set to 0

value_EF.set(0)
value_FLR.set(0)
value_LAS.set(0)

#Displays widgets for text, buttons, and text variables
#Buttons perform a command to add one to the current vote total
#This is viewed as a text variable in the row below
#Widgets have been allocated an appropriate sticky for resizing the position of the widget

text_A = ttk.Label(root, text = "Select the farm you believe in most need of aid:")
text_A.grid(column = 0, row = 0, columnspan = 3, sticky =(E, N, S, W))

elif_Farm = ttk.Button(root, text = "Elif Farm", command = add_One_Elif_Farm)
elif_Farm.grid(column = 0, row = 1, sticky =(E, N, S, W))

elif_Farm_Total = ttk.Label(root, textvariable = value_EF)
elif_Farm_Total.grid(column = 0, row = 2)

for_Loop_Range = ttk.Button(root, text = "For Loop Range", command = add_One_For_Loop_Range)
for_Loop_Range.grid(column = 1, row = 1, sticky =(E, N, S, W))

for_Loop_Range_Total = ttk.Label(root, textvariable = value_FLR)
for_Loop_Range_Total.grid(column = 1, row = 2)

list_Append_Stud = ttk.Button(root, text = "List Append Stud", command = add_One_List_Append_Stud)
list_Append_Stud.grid(column = 2, row = 1, sticky =(E, N, S, W))

list_Append_Stud_Total = ttk.Label(root, textvariable = value_LAS)
list_Append_Stud_Total.grid(column = 2, row = 2)

#Puts space around each widget

for child in root.winfo_children():
	child.grid_configure(padx = 5, pady = 5)

root.mainloop()
