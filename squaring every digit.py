number = 78432674

def square_numbers(number):
    items = [str(int(i)**2) for i in str(number)] #makes a string of given number, iterates over it, squaring each digit
    return int("".join(items)) #iterates over each digit, makes it a string - joins everything together, then transforms whole output into int

print(square_numbers(number))