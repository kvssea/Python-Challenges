'''presidents.py 
●	For this assignment, use the president_heights.csv file found in the Brightspace module.  You *WILL NOT NEED TO SUBMIT THE FILE TO CODEGRADE*
●	Create a program, presidents.py, that takes two arguments.  These arguments will correspond to the start and stop of a slice, respectively.  It will slice the heights column in the president_heights.csv files.  
●	Then print off the average height, rounded to two decimals, of the selected presidents in the following form:

The average height of presidents number x to y is z

	Where:
●	x = start of the slice
●	y = end of the slice
z = calculated average
'''

#presidents.py
import pandas as pd  
prez = pd.read_csv('president_heights.csv')

def presidents(start, stop):
    avg_height= sum(prez['height(cm)'][start:stop])
    
    print(f'The average height of presidents number {start} to {stop} is {avg_height:.2f}')



