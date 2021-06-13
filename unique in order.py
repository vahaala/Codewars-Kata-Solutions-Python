iterable = "AAAABBBCCDAABBB"

def unique_in_order(iterable):
    new_list = [] #makes empty list
    for item in iterable: #iterates over iterable
        if len(new_list) < 1 or item != new_list[len(new_list) - 1]: #if the list is empty, or the item is not equal to current last index in the list:
            new_list.append(item) #adds the item to the end of the list
    return new_list #returns list
print(unique_in_order(iterable))