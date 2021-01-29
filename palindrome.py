'''Create a program, palindrome.py, that has a function that takes one string argument and prints a sentence indicating if the text is a palindrome.  The function should consider only the alphanumeric characters in the string, and not depend on capitalization, punctuation, or whitespace.

	If your string is a palindrome it should print:

	It’s a palindrome!

	If it is not a palindrome, it should print:

	It’s not a palindrome! '''


#palindrome.py
def palindrome(word):
  word = word.replace(" ", "").lower()
  new_dict = {}
  for letter in word:
    new_dict.update({letter : word.count(letter)})
  
  odd_count = 0
  
  for item in new_dict.values():
    if item % 2 != 0:
      odd_count += 1
      
  if odd_count > 1:
    print("It's not a palindrome!")
   
  else:
    print("It's a palindrome")



