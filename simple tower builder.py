n_floors = 6

def tower_builder(n_floors):
    star = "*" #defines a bulding material
    tower = [] #builds empty tower
    total_width = (n_floors * 2) - 1 #defines max width of the tower
    for floor in range(n_floors): #iterates through floors
        width = (floor * 2) + 1 #defines width of the floor
        build = (star * width).center(total_width) #puts a centered floor, with max width as defined above
        tower.append(build) #adds the current floor to the tower
    return "\n".join(tower) #joins the list with a line break so the final result looks like a tower/pyramid
print(tower_builder(n_floors))