import tkinter as ttk
from tkinter import *
import random
 
root = Tk()
 
root.geometry("1000x600")

root.title("GUESS THE NUMBER ")


computer_value = {
    "1":"1",
    "2":"2",
    "3":"3",
    "4":"4",
    "5":"5",
    "6":"6",
    "7":"7",
    "8":"8",
    "9":"9",
    "10":"10"
}
 
# reset game  to play game again and again
def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    b4["state"] = "active"
    b5["state"] = "active"
    b6["state"] = "active"
    b7["state"] = "active"
    b8["state"] = "active"
    
    l1.config(text = "You")
    l3.config(text = "Computer Value")
    l4.config(text = "")
    
# disable button so that user can choose only one
def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"
    b4["state"] = "disable"
    b5["state"] = "disable"
    b6["state"] = "disable"
    b7["state"] = "disable"
    b8["state"] = "disable"

# is selected value is one
def is_one():
    cv=computer_value[str(random.randint(1,10))]
    if cv=='1':              # check whether computer value is equal to guesssed vaule or not
        res="YOU WIN"
    else:
        res="YOU LOOSE"
    l4.config(text = res)
    l1.config(text = "1")
    l3.config(text = cv)
    button_disable()
    
# is selected value is two
def is_two():
    cv=computer_value[str(random.randint(1,10))]
    if cv=='2':             # check whether computer value is equal to guesssed vaule or not
        res="YOU WIN"
    else:
        res="YOU LOOSE"
    l4.config(text = res)
    l1.config(text = "2")
    l3.config(text = cv)
    button_disable()
    
# is selected value is three
def is_three():
    cv=computer_value[str(random.randint(1,10))]
    if cv=='3':               # check whether computer value is equal to guesssed vaule or not
        res="YOU WIN"
    else:
        res="YOU LOOSE"
    l4.config(text = res)
    l1.config(text = "3")
    l3.config(text = cv)
    button_disable()

# is selected value is four  
def is_four():
    cv=computer_value[str(random.randint(1,10))]
    if cv=='4':             # check whether computer value is equal to guesssed vaule or not
        res="YOU WIN"
    else:
        res="YOU LOOSE"
    l4.config(text = res)
    l1.config(text = "4")
    l3.config(text = cv)
    button_disable()
   
# is selected value is five 
def is_five():             
    cv=computer_value[str(random.randint(1,10))]
    if cv=='5':              # check whether computer value is equal to guesssed vaule or not
        res="YOU WIN"
    else:
        res="YOU LOOSE"
    l4.config(text = res)
    l1.config(text = "5")
    l3.config(text = cv)
    button_disable()
    
# is selected value is six
def is_six():
    cv=computer_value[str(random.randint(1,10))]
    if cv=='6':             # check whether computer value is equal to guesssed vaule or not
        res="YOU WIN"
    else:
        res="YOU LOOSE"
    l4.config(text = res)
    l1.config(text = "6")
    l3.config(text = cv)
    button_disable()
    
# is selected value is seven
def is_seven():
    cv=computer_value[str(random.randint(1,10))]
    if cv=='7':              # check whether computer value is equal to guesssed vaule or not
        res="YOU WIN"
    else:
        res="YOU LOOSE"
    l4.config(text = res)
    l1.config(text = "7")
    l3.config(text = cv)
    button_disable()
 
# is selected value is eight   
def is_eight():
    cv=computer_value[str(random.randint(1,10))]
    if cv=='8':               # check whether computer value is equal to guesssed vaule or not
        res="YOU WIN"
    else:
        res="YOU LOOSE"
    l4.config(text = res)
    l1.config(text = "8")
    l3.config(text = cv)
    button_disable()
    
    
# is selected value is nine
def is_nine():
    cv=computer_value[str(random.randint(1,10))]
    if cv=='9':               # check whether computer value is equal to guesssed vaule or not
        res="YOU WIN"
    else:
        res="YOU LOOSE"
    l4.config(text = res)
    l1.config(text = "9")
    l3.config(text = cv)
    button_disable()
    
    
# is selected value is ten
def is_ten():
    cv=computer_value[str(random.randint(1,10))]
    if cv=='10':              # check whether computer value is equal to guesssed vaule or not
        res="YOU WIN"
    else:
        res="YOU LOOSE"
    l4.config(text = res)
    l1.config(text = "10")
    l3.config(text = cv)
    button_disable()

# add labels
Label(root,
      text = "NUMBER GUESSING GAME",
      font = "normal 30 bold",
      fg = "black").pack(pady =40)
               

frame = Frame(root)
frame.pack()
 
l1 = Label(frame,
           text = "YOU            ",
           font = 10)
 
l2 = Label(frame,
           text = "            VS             ",
           font = "normal 10 bold")
 
l3 = Label(frame, text = "      Computer", font = 10)
 
l1.pack(side = LEFT)
l2.pack(side = LEFT)
l3.pack()
 
l4 = Label(root,
           text = "",
           font = "normal 20 bold",
           bg = "white",
           width = 15 ,
           borderwidth = 2,
           relief = "solid")
l4.pack(pady = 20)
 
frame1 = Frame(root)
frame1.pack()


# add buttons
b1 = Button(frame1, text = "1",
            font = 10, width = 7,
            command = is_one)
 
b2 = Button(frame1, text = "2 ",
            font = 10, width = 7,
            command = is_two)
 
b3 = Button(frame1, text = "3",
            font = 10, width = 7,
            command = is_three)

b4 = Button(frame1, text = "4",
            font = 10, width = 7,
            command = is_four)


b5 = Button(frame1, text = "5",
            font = 10, width = 7,
            command = is_five)
 
b6 = Button(frame1, text = "6",
            font = 10, width = 7,
            command = is_six)

 
b7 = Button(frame1, text = "7",
            font = 10, width = 7,
            command =is_seven)
 
b8 = Button(frame1, text = "8",
            font = 10, width = 7,
            command = is_eight)

b9 = Button(frame1, text = "9",
            font = 10, width = 7,
            command =is_nine)
 
b10 = Button(frame1, text = "10",
            font = 10, width = 7,
            command = is_ten)
 
 
b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT,padx = 10)
b3.pack(side = LEFT,padx = 10)
b4.pack(side = LEFT, padx = 10)
b5.pack(side = LEFT,padx = 10)
b6.pack(side = LEFT,padx = 10)
b7.pack(side = LEFT, padx = 10)
b8.pack(side = LEFT,padx = 10)
b9.pack(side = LEFT,padx = 10)
b10.pack(side = LEFT, padx = 10)

Button(root, text = "Reset",
       font = 10, fg = "red",
       bg = "black", command = reset_game).pack(pady = 20)
 
                                                             
root.configure(bg='light blue')

root.mainloop()