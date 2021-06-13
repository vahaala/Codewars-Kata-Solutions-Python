test = ([13, 19, -1, 14, 16, -5, -3, 19, 9, 1], [11, 14, -17, 3, -15, -14, 20, 10, 5, -8])

def array_diff(a, b):
    return [i for i in a if i not in b] #iterates over first list, and constructs a new list with elements added to it only if they're not in second list

print(array_diff(test[0], test[1]))