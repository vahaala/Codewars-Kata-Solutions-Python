import string as str
from collections import Counter
string = "asdfg"
def is_isogram(string):
    new_string = string.lower() #transforms string into all lowercase, effectively ignoring the casing
    counter = Counter(new_string) #creates a dictionary of all letters in the string, and how many of each letter is in that string
    for value in counter.values(): #iterates through the dictionary values
        if value > 1: #checks for multiple occurrences
            return False
    else:
        return True

print(is_isogram(string))
            

