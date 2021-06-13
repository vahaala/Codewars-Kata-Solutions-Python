s = "abcDEFghi,,,,,321jklmnopqrstuvwxy    z!!"

def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz" #a string of alphabet letters
    for letter in s: #iterates over string
        alphabet = alphabet.replace(letter.lower(), "") #elimination based approach : pops a letter of alphabet that has been used at least once
    if alphabet == "": #if the alphabet is empty (every letter used at least once):
        return True
    else: #if at the end, there are still some letters left:
        return False

print(is_pangram(s))