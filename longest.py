'''Create a program, longest.py, that has a function that takes one string argument and prints a sentence indicating the longest word in that string.  If there is more than one word print only the first.  Your print statement should read:

The longest word is x

Where x = the longest word.  The word should be all lowercase.'''

#longest.py
def longest(string1):
    words = string1.split()
    lengths = list(map(len, words))
    i = lengths.index(max(lengths))
    print(f'The longest word is {words[i]}')



