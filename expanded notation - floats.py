number = 3210032131.5403545
def expand_form(number):
    split = str(number).split(".") #transforms the number into a string, and splits it into decimal and integer parts on the dot
    wholes = [i for i in split[0]] #creates a list that contains the integer part of the number
    dec = [i for i in split[1]] #creates a list that contains the fractional part of the number
    list_wholes = [] #creates an empty list, for storing the results of iterating on integer part
    list_decimals = [] #as above, but for decimal part
    for index, item in enumerate(wholes[::-1], start = 1): #iterates through the wholes list with enum(), going right to left and initial enum index set to 1
        decimals = (10 ** index) * int(item) #transforms a digit into a power of 10, like "3" in third place from the right = "3000"
        if item != "0": #if the current integer digit is not zero:
            list_wholes.append(f"{decimals}") #appends it to the results list
    list_wholes.reverse() #reverses the list, so the biggest numbers will go in the front
    for index, item in enumerate(dec, start = 1): #iterates through the decimals list with enum(), starting at index 1
        decimals = 10 ** index #defines the powers of 10
        if item != "0": #if the current decimal number is not zero:
            list_decimals.append(f"{item}"+"/"+f"{decimals}") #creates the "x/y" notation, that first appends the current digit and then after a slash it's power of 10. appends it to the list
    final_list = list_wholes + list_decimals #joins the lists of wholes and decimals into one list
    return " + ".join(final_list) #joins the final list together into a string and returns that value to the function
print(expand_form(number))