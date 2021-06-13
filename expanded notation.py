number = 2183000000621579843658472093274892367842482390579546234802374237907

def expand_form(number):
    number_list = [int(i) for i in str(number)] #creates a list from given integer so we can iterate over it
    empty_list=[] #creates an empty list, for storing the results
    length = len(number_list) #calculates a length of the numbers list, to define maximum number of zeros to be added
    for i in number_list: #iterates through numbers list
        number_of_zeros = (length - 1) * "0" #calculates how many zeros we should add at the end of each number
        length -= 1 #shortens the zeros by a decimal place, equivalent of dividing by 10
        if i != 0: #checks if the current number isn't 0, indicating "zero thousands/hundreds/whatevers", if it is - skips adding them to the list
            empty_list.append(f"{i}"+f"{number_of_zeros}") #appends the result into new list
    list_string = " + ".join(empty_list) #joins the list into a string with " + "
    return list_string
print(expand_form(number))