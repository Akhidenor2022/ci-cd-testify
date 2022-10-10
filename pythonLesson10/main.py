# 1. Create an anonymous function that prints out Hello World
# 2. Invoke/call the function

print("Anonymous function")


def greet():
    print("Hello World")


def accept(bb):
    bb("Hello")


hello = lambda : print("Hello World Together")
hello()
accept(lambda x: print(x))
