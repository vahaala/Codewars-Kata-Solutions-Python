ppl = [[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]

def people_on_bus(ppl):
    starting = 0 #sets the amount of passengers already in bus to 0
    for item in ppl: #iterates over the list of pairs
        people_in = item[0] #first number in pair is how many people hop in
        people_out = item[1] #second is how many get out
        starting += people_in #adds how many people hop in to the starting value
        starting -= people_out #and then substracts how many ppl hop out
    return starting #returns the final value

print(people_on_bus(ppl))