'''●	Create program called reallyrandom.py that has a function that takes in three arguments and prints one integer.  Your random seed should be set to 42.
○	The first argument should correspond to the size of a np.randint that has values from 0 to 10.  
○	The second is an integer that you will multiply the randint by.  
○	The third argument is a value you will index the result of the multiplication by. 
●	You will print the integer that was indexed as ‘Your random value is x’ where x = the result of the indexing.
●	The program should not crash if the third value is larger than the first.
Example:

python3 reallyrandom.py 59 2 7 

Should generate the following:

Your random value is 12'''

#reallyrandom.py
import numpy as np 

def reallyrandom(sizer, factor, index):
    np.random.seed(42)
    rand = np.random.randint(0, 10, size = sizer)
    rand = 2 * rand
    print(rand[index])
    print("It's a palindrome")



