all_names = ["Romario", "Boby", "Roosevelt", "Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

# Your code here

def names(list):
    return list[0].lower() == "r"

resulting_names = list(filter(names, all_names))

print(resulting_names)




