# Chapter 18: Classes and Objects (Deep Dive)

This chapter covers more advanced OOP concepts like overloading, equality, and object mutability.

## 1. Pure Functions vs. Modifiers
* **Pure Function:** Takes objects as arguments and returns a *new* object. Does not change the originals. (Functional programming style).
* **Modifier:** Changes the state of an object (self) directly. Returns None (usually).

## 2. Operator Overloading
You can define how standard Python operators work with your custom objects by defining special "dunder" (double underscore) methods.

* `__add__(self, other)`: Enters when you use +
* `__sub__(self, other)`: Enters when you use -
* `__mul__(self, other)`: Enters when you use *
* `__eq__(self, other)`: Enters when you use ==

**Example:**

    def __add__(self, other_point):
        return Point(self.x + other_point.x, self.y + other_point.y)

## 3. Polymorphism
* Functions that work with different types of input.
* If your class has `__add__` and `__str__`, many standard Python functions (like sum or print) will work on your objects automatically.

## 4. Deep vs. Shallow Equality
* **Shallow Equality (`is`):** Checks if two variables refer to the exact same memory address.
    * `p1 is p2` is False, even if they have the same data.
* **Deep Equality (`==`):** Checks if the *contents* are the same.
    * You must implement the `__eq__` method in your class for this to work correctly. Without it, == usually defaults to checking identity (like `is`).