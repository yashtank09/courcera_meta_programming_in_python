# creating a class using `class` keyword and name is MyClass here
# everything we are typing is process of instantiating
class MyClass:
    # creating an attribute
    a = "This is an attribute."

    def hello(self): # TypeError: hello() takes 0 positional arguments but 1 was given when we don't write self as an argument
        print("Hello behaviour!")
    # printing string
    print("Hello Class!")
    # pass keyword plays the role of a placeholder when nothing needs to be executed.
    pass


# instance/ object of class
mc = MyClass()

# calling attribute using class name
print(MyClass.a)  # print(a) will not work

# calling attribute using instance object
print(mc.a)

# calling function that encapsulated inside the class
print(mc.hello())
