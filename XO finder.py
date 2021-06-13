import re
string = "abcdegfhxxxooo"

def getXO(string):
    numX = len(re.findall("[x]+", string, re.IGNORECASE)) #RegEX to find all X's, case insensitive. immediately returns the length because of len()
    numO = len(re.findall("[o]+", string, re.IGNORECASE)) #as above but for Y's
    if numX == numO: #checks if the number of X and O's is equal
        return True
    else:
        return False

print(getXO(string))