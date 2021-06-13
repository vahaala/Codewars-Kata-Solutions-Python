import re #imports RegEx module
text = "1Testing-1234-abcd-Test-Test"

def camel_case(text):
    split = re.split("[^a-zA-Z0-9]", text) #splits the string into list of separate words on anything that's not a letter or number using RegEx
    if split[0] != split[0].capitalize: #checks if the first element isn't capitalized
        for index, item in enumerate(split[1::], start = 1): #enumerates through the list, skipping the first element
            split[index] = item.capitalize() #capitalizes everything except the first word
    else: #if it is capitalized:
       for index, item in enumerate(split): #enumerates through all elements of the list
           split[index] = item.capitalize() #capitalizes every element
    camel_case = "".join(split) #joins the list into CamelCase
    return camel_case

print(camel_case(text))