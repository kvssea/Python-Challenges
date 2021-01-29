'''Create a program inrange.py that has a function that takes one integer argument. 
 The function will print a list of all values between 5000 and 8000 that is 
 divisible by (1) the integer argument, and (2) the argument + 4.'''

#inrange.py
def inrange(int1):
    ranges = range(5000,8000)
    output = []
    for number in ranges:
        if (number % int1 == 0) and (number % (int1 + 4) == 0):
            output.append(number)
    print(output)


