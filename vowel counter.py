import re

input_str = "t3est test dasadgvhjasbdvgyutgbewyjsvfyu hbybyaaaaaAAAAAaaaaAAAAAOOOTITUAISAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAbyaadsagdasdasdasadaaaaaaaaoootuutyeuiwwoooo"

def get_count(input_str):
    search = re.compile("[aeiou]", re.IGNORECASE) #creates RegEX instance to find all matches, case insensitive
    length = search.findall(input_str) #uses RegEX we created earlier, to find all wovels and put them in a list
    num_vowels = len(length) #counts the length of the list above
    return num_vowels #returns the result

print(get_count(input_str))