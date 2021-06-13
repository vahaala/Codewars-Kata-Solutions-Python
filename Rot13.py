string = "The sly fox, gets the most eggs."

empty_list = [] #makes a new list for storing the results
def rot13(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz" #defines lowercase alphabet
    alphabet_translated = "".join([alphabet[(alphabet.find(i) + 13) % 26] for i in alphabet]) #defines translated alphabet
    for letter in string: #iterates over given string
        if letter.islower(): #if current letter is lowercase:
            find = alphabet.find(letter) #finds the index of the letter in alphabet (as in, which letter of the alphabet it is)
            empty_list.append(alphabet_translated[find]) #appends a letter of matching index from translated alphabet
        elif letter.isupper(): #if the letter is uppercase:
            find = alphabet.upper().find(letter) #does the same thing as above, but using upper() to transform alphabets into uppercase
            empty_list.append(alphabet_translated[find].upper())
        else: #if it's not a letter (a digit, whitespace, punctuation):
            empty_list.append(letter) #append it as is
    return "".join(empty_list) #returns the result list joined into a string
    

print(rot13(string))
