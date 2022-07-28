# Source: Python Programming for the Absolute Beginner, Third Editiogit n, Michael Dawson.
# Source: https://www.plus2net.com/python (Video)

import tkinter as tk


def input_choice_display():
    my_w = tk.Tk()
    my_w.geometry('400x200')  # To specify size
    my_w.title('Input Type selection')
    font1 = ('Times', 14, 'bold')
    font2 = ('Times', 12, 'bold')

    l1 = tk.Label(my_w, text='Choices to input point coordinates', font=font1).grid(row=1, column=1)

    l2 = tk.Label(my_w, text='\n    Choices are:', font=font2).grid(row=2, column=1)
    l3 = tk.Label(my_w, text='\nChoice 1: CSV File').grid(row=3, column=1)
    l4 = tk.Label(my_w, text='             Choice 2: Keyboard Input').grid(row=4, column=1)
    eb = tk.Button(my_w, text='Click to exit', command=my_w.quit).grid(row=6, column=2)
    my_w.mainloop()

