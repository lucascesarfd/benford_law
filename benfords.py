"""
File: benfords.py

Author: Lucas Cesar
Year: 2020
"""
import tkinter
from dataclasses import dataclass
from tkinter import BOTH

navy_blue='#030f30'
light_blue='#a6ffdd'


@dataclass
class generalSizes:
    height: int = 500
    width: int = 800


def calculateWdnSize(window,screen):
    window.height = round(screen.height/2.5)
    window.width = round(screen.width/3)

def guiWindow(wdn):
    # Define root window
    main_window = generalSizes()
    main_screen = generalSizes()

    # Calculate the center of the screen
    main_screen.width = wdn.winfo_screenwidth()
    main_screen.height = wdn.winfo_screenheight()

    calculateWdnSize(main_window,main_screen)

    x_cordinate = int((main_screen.width/2) - (main_window.width/2))
    y_cordinate = int((main_screen.height/2) - (main_window.height/2))

    # Define the eindows properties
    wdn.title('Benford\'s Law')
    wdn.iconbitmap('Math.ico')
    wdn.resizable(True,True)
    wdn.config(bg=navy_blue)
    wdn.geometry("{}x{}+{}+{}".format(main_window.width, main_window.height, x_cordinate, y_cordinate))

def benfordLogic(wdn):
    occurrence_values = {
    "one":0,
    "two":0,
    "three":0,
    "four":0,
    "five":0,
    "six":0,
    "seven":0,
    "eight":0,
    "nine":0
    }

    file_name = "dados2019.csv"
    file_total_lines = 0

    wdn.config(text = "File Name: "+file_name)

    file = open(file_name, 'r')

    for line in file:
        file_total_lines += 1
        line_components = line.split(';')
        if line_components[1][0]=='1':
            occurrence_values["one"]+= 1
        if line_components[1][0]=='2':
            occurrence_values["two"]+= 1
        if line_components[1][0]=='3':
            occurrence_values["three"]+= 1
        if line_components[1][0]=='4':
            occurrence_values["four"]+= 1
        if line_components[1][0]=='5':
            occurrence_values["five"]+= 1
        if line_components[1][0]=='6':
            occurrence_values["six"]+= 1
        if line_components[1][0]=='7':
            occurrence_values["seven"]+= 1
        if line_components[1][0]=='8':
            occurrence_values["eight"]+= 1
        if line_components[1][0]=='9':
            occurrence_values["nine"]+= 1

    file.close()

    for key, value in occurrence_values.items():
        percentage = (value/file_total_lines)*100
        value_label = tkinter.Label(wdn, text=key.capitalize() + ": " + str(round(percentage,2)) + "%",fg=light_blue, bg=navy_blue)
        value_label.pack()


"""
The Main Code starts here!
"""
root = tkinter.Tk()
guiWindow(root)

titles_frame = tkinter.Frame(root, bg=navy_blue)
titles_frame.pack(fill=BOTH,expand=True)

results_frame = tkinter.LabelFrame(root, bg=navy_blue)
results_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Insert a Label with the title
title_label = tkinter.Label(titles_frame, text="Benford\'s Law", fg=light_blue, bg=navy_blue,font=('Arial',18,'bold'))
title_label.pack(pady=(5,20))

benfordLogic(results_frame)

title_label.pack()

# Start the GUI loop
root.mainloop()
