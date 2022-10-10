# 1. Declare a dictionary with any key-value pair of items/elements
# 2. Print the dictionary in console
# 3. Update the dictionary with two different key-value pair items
# 4. Print the dictionary in console again
#  Note: you can experiment with the other list functions too in the task.


liquid ={
    "Water": "Nestle",
    "Edible oil": "Juice",
    "Benzene": "Petroleum"
}
print("dictionary:", liquid)

# update - add more liquid
liquid.update({"Wine": "Grenache"})
liquid.update({"Milk": "Dano"})
print("update:", liquid)

# copy - return a copy of a dictionary
copied_liquid = liquid.copy()
print("copy:", copied_liquid)



