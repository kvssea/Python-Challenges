'''●	Create a program, digits.py, that has a function 
that takes a number and prints the number of digits in the number. 
 It should work for numbers with decimals, too.
'''

#digits.py
def digits(number):
    number = str(number)
    digits = 0
    for num in number:
        if num in map(str, list(range(9))):
            digits += 1
    print(digits)




