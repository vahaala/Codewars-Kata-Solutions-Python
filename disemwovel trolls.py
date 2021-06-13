import re

txt = "This website is for losers LOL!"

def disemvowel(txt):
    find = re.compile("[^aeiouAEIOU]") #uses RegEx to find all characters that are *not* vowels, upper or lowercase (for this kata purpose)
    new_string = "".join([i for i in txt if i in find.findall(txt)]) #creates a new string, by making a list that adds every letter in above regex, and joins it
    return new_string #returns new string

print(disemvowel(txt))