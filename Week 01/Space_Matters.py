"""
Spacing is matters
"""

# Correct: any amount of whitespace on a single line is ok
x  =     1     +     2
print(x)

# Incorrect
x = 1 + 2
+ 4

"""
Indentation
"""

# Correct
def say_Hello():
    print("Hello World!")

print(say_Hello())

# declaration is case sensitive
def say_hello(): print("Hello there!")

print(say_hello())
"""
# Incorrect
def sayHello():
print("Say Hello")

    def sayhello():
print("say hello")
"""
