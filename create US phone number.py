number = [6, 6, 6, 1, 3, 4, 8, 0, 9, 0]
def create_phone_number(number):
    first = "".join([str(num) for num in number[:3:]]) #creates a joined string of first three numbers in the array
    next = "".join([str(num) for num in number[3:6:]]) #same but for next three
    last = "".join([str(num) for num in number[6::]]) #same but for the rest
    phone_number = "(" + f"{first}" + ") " + f"{next}" + "-" + f"{last}" #joins it all together into a string, first three numbers in parenthesis and dash inbetween rest
    if len(number) == 10:
        return phone_number
    else:
        return "You need to provide a valid array."
    
print(create_phone_number(number))