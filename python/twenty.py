# Define a function named "larger_string" that takes two parameters, "text" and "n"
def larger_string(text, n):
    result = ""

    for i in range(n):
        result = result + text
    return result

print(larger_string('abc', 2))

print(larger_string('.py', 3))

# output:
# abcabc
# .py.py.py