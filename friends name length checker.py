x = ["Mark", "Jonathan", "Chris", "Olek", "Maciek", "Kuba"]
def friends(x):
    return [i for i in x if len(i) == 4]
print(friends(x))