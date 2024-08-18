# We create a class called Dog, with a method called bark.
# self as an argument of the method, will point to the current object. It must be specified when defining a method inside a class.
# __init__ is a special type of method, it is a constructor. As such, it also needs the "self" argument"
class Dog:
    def __init__(self, name, age):
        self.name = name    # self.name is the name attribute of this instance of object being created.
        self.age = age

    def bark(self):
        print("woof!")

roger = Dog("Roger", 8)

print(roger.name)
print(roger.age)
roger.bark()