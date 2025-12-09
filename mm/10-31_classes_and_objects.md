# Chapter 17: Classes and Objects (Basics)

This chapter introduces **Object-Oriented Programming (OOP)**, allowing users to define their own data types.

## 1. Terminology
* **Class:** A factory/blueprint for creating objects (e.g., Point).
* **Object (Instance):** A specific realization of a class (e.g., a specific point at 3,4).
* **Instantiation:** The act of creating an object from a class.

## 2. Defining a Class

    class Point:
        """ Represents a point in 2D space """
        def __init__(self, x=0, y=0):
            self.x = x  # Attribute
            self.y = y  # Attribute

## 3. The `__init__` Method (Constructor)
* A special method that runs automatically when a new object is created.
* Used to set up initial **attributes** (state).

## 4. The `self` Parameter
* `self` is the first parameter of every method in a class.
* It is a reference to the **current object** being accessed or modified.
* Example: p.x translates to self.x inside the class definition.

## 5. Adding Methods
Functions defined inside a class are called methods.
* **`__str__` method:** Another special method. It must return a string. It defines what happens when you call print(my_object) or str(my_object).

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)