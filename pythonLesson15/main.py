# 1. Declare a list with any value and number of item/element
# 2. Print the list in console
# 3. Sort the list
# 4. Print the list in console again


languages = ["One", "Two", "Three", "Four", "6", '7']
print("list:", languages)


languages.append("Numbers")
print("append:", languages)


# sort item/element

languages.sort()
print("sort-asc:", languages)


# insert add new item/element
languages.insert(0, "Zero")
languages.insert(6, "Five")
print("insert:", languages)

# remove an item/element
languages.remove("Three")
print("remove:", languages)

# count item/element






