# 1. Create a function that prints out Hello World
# 2. Invoke the same function in it own body
# 3. Invoke the function outside the function block


def print_hello():
    print("Hello World")
    print_hello()

print_hello()
