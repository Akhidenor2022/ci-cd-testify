# 1. Declare a global variable with name as language and the value as Python
# 2. Create a function, in the function declare a variable with name as language and value as Java, then print out the variable in the function
# 3. Print out the variable name into the console
# 4. Invoke the function

name = "Python" # global variable


def greet():
    language = "Java"
    print("name", name, "language", language)
    print(name)


greet()
