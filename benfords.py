"""
File: benfords.py

Author: Lucas Cesar
Year: 2020
"""

file_name = "dados2010.csv"
file_total_lines = 0
occurence_values = {
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

file = open(file_name, 'r')

for line in file:
    file_total_lines += 1
    line_components = line.split(';')
    if line_components[1][0]=='1':
        occurence_values["one"]+= 1
    if line_components[1][0]=='2':
        occurence_values["two"]+= 1
    if line_components[1][0]=='3':
        occurence_values["three"]+= 1
    if line_components[1][0]=='4':
        occurence_values["four"]+= 1
    if line_components[1][0]=='5':
        occurence_values["five"]+= 1
    if line_components[1][0]=='6':
        occurence_values["six"]+= 1
    if line_components[1][0]=='7':
        occurence_values["seven"]+= 1
    if line_components[1][0]=='8':
        occurence_values["eight"]+= 1
    if line_components[1][0]=='9':
        occurence_values["nine"]+= 1

file.close()

for value in occurence_values.values():
    percentage = (value/file_total_lines)*100
    print(percentage)

    
