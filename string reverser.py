string = "hellio"

def solution(string):
    new_string = string[-1::-1] #copies the string into a new one, starting from the end and going backwards 
    return new_string #returns the new, reversed string
print(solution(string))