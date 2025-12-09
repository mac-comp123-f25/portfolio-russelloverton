# Chapter 12: Dictionaries

Dictionaries are Python's built-in **mapping type**. Unlike lists, which use integer indices, dictionaries use **keys** (which can be any immutable type) to look up **values**.

## 1. Basic Syntax
* **Creation:** my_dict = {'key1': 'value1', 'key2': 'value2'}
* **Empty Dict:** my_dict = {}
* **Accessing:** print(my_dict['key1']) -> outputs 'value1'

## 2. Mutability
Dictionaries are mutable.
* **Add/Update:** my_dict['new_key'] = 'new_value'
    * If 'new_key' exists, the value is updated.
    * If not, the pair is added.
* **Delete:** del my_dict['key']

## 3. Dictionary Methods
* .keys(): Returns a view of the keys.
* .values(): Returns a view of the values.
* .items(): Returns a list of (key, value) tuples.
* .get(key, default): Safely retrieves a value. Returns `default` if the key is missing (prevents KeyErrors).

## 4. Aliasing and Copying
* Because dictionaries are mutable, assigning d2 = d1 creates an **alias**. Both variables point to the same object.
* To copy, use the .copy() method.

## 5. Sparse Matrices
Dictionaries are useful for representing matrices that contain mostly zeros.
* **Key:** A tuple representing coordinates (row, col).
* **Value:** The non-zero number.
* **Example:** matrix = {(0, 3): 1, (2, 1): 5}
    * To lookup: matrix.get((0,3), 0) (Returns 0 if the coordinate isn't stored).

## 6. Counting with Dictionaries (Histograms)
A very common pattern is using a dictionary to count frequency of items in a list/string.

    counts = {}
    for letter in "mississippi":
        counts[letter] = counts.get(letter, 0) + 1