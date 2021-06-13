array = [[1, 2, 3, 3]
       , [4, 5, 6, 6],
         [7, 8, 9, 8],
         [4, 4, 4, 4]]

def snail_path(array):
    return list(array[0]) + snail_path(list(zip(*array[1::]))[::-1]) if array else [] #returns the first array element, then uses zip() to iterate over others

print(snail_path(array))