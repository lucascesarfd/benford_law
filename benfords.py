"""
File: benfords.py

Author: Lucas Cesar
Year: 2020
"""
import tkinter
from dataclasses import dataclass

navyBlue='#030f30'
lightBlue='#a6ffdd'


@dataclass
class generalSizes:
    height: int = 500
    width: int = 800


def calculateWdnSize(window,screen):
    window.height = round(screen.height/2.5)
    window.width = round(screen.width/3)

def guiWindow(wdn):
    # Define root window
    mainWindow = generalSizes()
    mainScreen = generalSizes()

    # Calculate the center of the screen
    mainScreen.width = wdn.winfo_screenwidth()
    mainScreen.height = wdn.winfo_screenheight()

    calculateWdnSize(mainWindow,mainScreen)

    xCordinate = int((mainScreen.width/2) - (mainWindow.width/2))
    yCordinate = int((mainScreen.height/2) - (mainWindow.height/2))

    # Define the eindows properties
    wdn.title('Benford\'s Law')
    wdn.iconbitmap('Math.ico')
    wdn.resizable(True,True)
    wdn.config(bg=lightBlue)
    wdn.geometry("{}x{}+{}+{}".format(mainWindow.width, mainWindow.height, xCordinate, yCordinate))

    # Insert a Label with the title
    titleLabel = tkinter.Label(wdn, text="Benford\'s Law", fg=navyBlue, bg=lightBlue,font=('Arial',18,'bold'))
    titleLabel.pack(pady=(0,20))

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

    file_name_label = tkinter.Label(wdn, text = "File Name: "+file_name, fg = navyBlue, bg = lightBlue, font = ('Arial', 12, 'bold'))
    file_name_label.pack(pady=(0,10))


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
        value_label = tkinter.Label(wdn, text=key.capitalize() + ": " + str(round(percentage,2)) + "%",fg=navyBlue, bg=lightBlue)
        value_label.pack()


"""
The Main Code starts here!
"""
root = tkinter.Tk()

guiWindow(root)
benfordLogic(root)

# Start the GUI loop
root.mainloop()
