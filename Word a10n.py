import re #imports RegEx
import string #imports string tools
s = "This is  ____   ))  %^%$ superexcalifrag55555ilisticexploadiocious!!!!!" #initial string
def abbreviate(s): #defines the function
    pattern = re.compile(rf"[a-zA-Z]+|[0-9]|[\s]|[{string.punctuation}]") #creates a RegEx pattern, that looks for any "words", and separately for any punctuation or numbers
    s = pattern.findall(s) #uses the pattern defined above on initial string
    new_list = [] #creates empty list to store abbreviations
    for word in s: #iterates over list of words and punctuations found by RegEx
        if len(word) >= 4 and string.punctuation not in word: #only performs abbreviations on words >= 4 letters or longer, excluding punctuation
            word = word[0] + str((len(word) - 2)) + word[-1] #creates abbreviated version of the word - first letter, number of removed letters, last letter
        new_list.append(word) #appends abbreviated words and (untouched) punctuation to temporary list
    new_s = "".join(new_list) #joins the resulting list
    return new_s #returns abbreviated list, with punctuation untouched
print(abbreviate(s))