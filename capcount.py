'''●	Create a program called capCount.py that has a function that takes in a string and prints the number of capital letters in it.  
It should work for both lowercase and uppercase vowels.
'''

#capCount.py
def capCount(string):
    cap_count = 0
    for letter in string:
        if ord(letter) in range(65,90):
            cap_count += 1
    print(cap_count)




