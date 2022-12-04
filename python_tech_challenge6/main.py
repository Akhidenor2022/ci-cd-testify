# Write a function that removes repeated characters from a string.
# Sample strings are: a Hello: Output should be Helo b. Concatenate: output should be Conaten


def repeated_charcters(p):
    q = ''
    for char in p:
        if char not in q.casefold():
         q += char

    print(q)
repeated_charcters('Concatenate')
repeated_charcters('Hello')