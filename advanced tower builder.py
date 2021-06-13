n_floors = 3
block_size = (4,2)

def tower_builder(n_floors, block_size):
    star = "*" #defines a bulding material
    tower = [] #builds empty tower
    total_width = ((n_floors * block_size[1]) * 2) - block_size[0] #defines max width of the tower
    for floor in range(n_floors): #iterates through floors
        width = (floor * 2) + 1 #defines width of the floor
        for block in range(block_size[1]): #iterates through, to build a block
            build = ((star * width)*block_size[0]).center(total_width) #puts a centered floor into a block, with max width as defined above
            tower.append(build) #adds the current floor to the tower
    return "\n".join(tower) #joins the list with a line break so the final result looks like a tower/pyramid
print(tower_builder(n_floors,block_size))