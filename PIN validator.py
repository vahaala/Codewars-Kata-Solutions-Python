import re
pin = "123456"

def validate_pin(pin):
    check = re.compile("[^0-9]") #creates a RegEx pattern, that returns a match if there are any non-number characters
    if len(str(pin)) in {4, 6} and len(check.findall(str(pin))) == 0: #checks if the length is equal to 4 or 6 digits, as well as if there are no characters other than digits
        return True
    else:
        return False

print(validate_pin(pin))