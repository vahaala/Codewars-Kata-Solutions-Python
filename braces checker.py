string = "(({({})}))"

def validBraces(string):
    parentheses = ["{}", "[]", "()"] #creates a list of valid parentheses
    while any(x in string for x in parentheses): #while there are still any parentheses left in the string:
        for bracket in parentheses: #iterates over bracket list to check for innermost valid ones:
            string = string.replace(bracket, "") #replace it with an empty string, eliminating it
    return not string #returns a bool, True if the end string is empty (all valid brackets removed), False if it's not

print(validBraces(string))
