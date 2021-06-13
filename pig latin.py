import re #imports RegEx
text = "I'm Commander Shepard, and this is my favourite shop on the Citadel !" 
def pig_it(text):
    pattern = re.compile(r"[^a-zA-Z0-9]") #a RegEx pattern to look for any character that is not a letter or digit
    new_list = [] #list to store results
    split = text.split() #splits given string on a whitespace
    for item in split: #iterates over split text
        finds = pattern.findall(item) #searches for RegEx pattern in current item (word)
        if item in finds: #if the last word is just punctuation:
            new_word = item #stores it for adding into list later
        elif item[-1] in finds: #if the last character is not a digit or letter:
            new_word = item[1:-1:] + item[0] + "ay" + item[-1] #new word is made: everything but first letter, until very last sign (punctuation) + first letter at the end + "ay" + punctuation 
        else: #if last character is a digit or letter:
            new_word = item[1::] + item[0] + "ay" #new word is made: everything but first letter + first letter at the end + "ay"
        new_list.append(new_word) #appends these new words in order to an empty list
    pig_latin = " ".join(new_list) #joins results using a whitespace
    return pig_latin
print(pig_it(text))