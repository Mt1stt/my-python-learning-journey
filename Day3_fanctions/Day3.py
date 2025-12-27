#Functions in Python is defined using the def keyword. it is used to encapsulate a block of code that performs a specific task. it allows for code reusability and modular programming.it can take inputs, process them, and return outputs.it helps in organizing code into manageable sections. making it easier to read, maintain, and debug. mainly functions are used to avoid code repetition and improve code organization.mainly two types of functions are there:inbuilt functions and user-defined functions.most common inbuilt functions are print(), input(), len(), type(), int(), str(), float(), list(), dict(), etc.most common user-defined functions are as follows:my_function(), calculate_sum(), greet_user(), find_maximum(), etc. 
# Built-in functions are already included in Python.

# Example: print() → displays output on the screen
print("Hello, Python!")

# Example: len() → counts how many items in a list or how many characters in a string
cities = ["Cairo", "Paris", "Tokyo"]
print(len(cities))  # Output: 3
# User-defined functions are created by the user to perform specific tasks.
# Example of a user-defined function
def greet_user(name):
    print("Hello, " + name + "!") 
greet_user("Alice")  # Output: Hello, Alice!
# Example of a user-defined function that calculates the sum of two numbers
def calculate_sum(a, b):
    return a + b   
result = calculate_sum(5, 10)
print(result)  # Output: 15

print(len("Hello, World!"))  # Output: 13

#len() number of characters in the string including spaces and punctuation
print(len("Python Functions"))  # Output: 17
#max() returns the largest item in an iterable or the largest of two or more arguments.
print(max(5, 10, 3))  # Output: 10
fam=[0,10,20,5] 
biggest=max(fam) # largest number among the three
print(biggest)

help(round)  # round() function rounds a floating-point number to a specified number of decimal places.
print(round(3.14159, 2))  # Output: 3.14
#abs() function returns the absolute value of a number.
print(abs(-7))  # Output: 7
print(abs(5))   # Output: 5
#sum() function returns the sum of all items in an iterable (like a list).
numbers = [1, 2, 3, 4, 5] 
print(sum(numbers))  # Output: 15


# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))


# Convert var2 to an integer: out2
out2 = int(var2)

help(pow)

#pow(base, exp, mod)
#base → the number you want to raise

#exp → the exponent (the power you raise it to)

#mod → (optional) a number to take the result “modulo” something (used in advanced math or cryptography)


# Example 1: without mod
print(pow(2, 3))  
# This means 2^3 = 8
# Example 2: with mod
print(pow(2, 3, 5))
# This means (2^3) % 5 = 8 % 5 = 3

help(sorted) 

# The sorted() function in Python is a built-in function that returns a new sorted list 
# from any iterable (like a list, tuple, or set).

# 🧩 Syntax:
# sorted(iterable, key=None, reverse=False)

# Parameters:
# iterable → The data you want to sort (like a list of numbers or strings).
# key → (optional) A function to decide how to sort the elements.
# reverse → (optional) If True, sorts in descending order (largest → smallest).
# By default, it’s False, meaning ascending order (smallest → largest).

# ✅ Example 1: Basic sorting
numbers = [5, 2, 9, 1]
print(sorted(numbers))
# Output: [1, 2, 5, 9]

# ✅ Example 2: Sorting in reverse order
print(sorted(numbers, reverse=True))
# Output: [9, 5, 2, 1]

# ✅ Example 3: Using the key parameter
words = ["apple", "Banana", "cherry"]
print(sorted(words, key=str.lower))
# Output: ['apple', 'Banana', 'cherry']
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full,reverse=True)

# Print out full_sorted
print(full_sorted)
# 🧩 Sorting Lists in Python

numbers = [5, 2, 9, 1, 7]

# 🔹 1. Ascending order (smallest → largest)
ascending = sorted(numbers)
print(ascending)  
# Output: [1, 2, 5, 7, 9]

# 🔹 2. Descending order (largest → smallest)
descending = sorted(numbers, reverse=True)
print(descending)
# Output: [9, 7, 5, 2, 1]

# ✅ Important: 'sorted()' creates a NEW sorted list and does not modify the original
print(numbers)  
# Output: [5, 2, 9, 1, 7] (still unchanged)

# 🔹 3. Using .sort() — sorts the list IN PLACE (modifies the original list)
numbers.sort()
print(numbers)  
# Output: [1, 2, 5, 7, 9]

# 🔹 4. .sort(reverse=True) — sorts in descending order (changes the list)
numbers.sort(reverse=True)
print(numbers)
# Output: [9, 7, 5, 2, 1]




#  What are Methods in Python?

# Methods are functions that belong to specific objects.
# In Python, everything is an object — strings, numbers, lists, etc.
# Each object type (like str, int, float, list, dict) has its own set of built-in methods.
# You call a method using a dot after the object name, like:
# object.method()

# 📘 Example 1: String methods
sister = "liz"
# capitalize() → makes the first letter uppercase
print(sister.capitalize())   # Output: Liz
# replace() → replaces a part of the string with another
print(sister.replace("l", "L"))   # Output: Liz

# 📘 Example 2: Float methods
height = 1.73
# as_integer_ratio() → returns numerator and denominator that represent the float
print(height.as_integer_ratio())  # Output: (173, 100)
# is_integer() → checks if the float is a whole number
print(height.is_integer())  # Output: False

# 📘 Example 3: List methods
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
# index() → returns the position of a specific value
print(fam.index("mom"))  # Output: 4# count() → counts how many times a value appears
print(fam.count(1.73))  # Output: 1

# ⚙️ Summary:
# • Strings (str) have methods like capitalize(), replace(), upper(), lower(), etc.
# • Floats (float) have methods like as_integer_ratio(), is_integer().
# • Lists (list) have methods like index(), count(), append(), remove(), sort(), etc.
# Methods are used to manipulate or get information from the object directly.

#Can you use .replace() on everything?

#No  — you cannot use .replace() on all data types.
#It works only on strings (str type).

#Because .replace() is a string method, not a list or number method.
#Each data type in Python (string, list, float, etc.) has its own methods.

# Example: Working correctly with strings
text = "I love Java"
new_text = text.replace("Java", "Python")
print(new_text)  # Output: I love Python


#Explanation:
#text is a string, so .replace() works and replaces "Java" with "Python".

#Example: Fails with lists
languages = ["Java", "C++", "Python"]
languages.replace("Java", "Python")  #  Error: 'list' object has no attribute 'replace'


#Lists don’t have a .replace() method — that’s why Python gives you an AttributeError. To “replace” in a list, you must use indexing:


languages[0] = "Python"
print(languages)  # Output: ['Python', 'C++', 'Python']

#but some methods can be used on multiple data types. for example: .count() method can be used on both strings and lists.
# Example: Using .count() on a string
sentence = "Python is great. I love Python."
print(sentence.count("Python"))  # Output: 2

# Example: Using .count() on a list
languages = ["Java", "C++", "Python", "Java"]
print(languages.count("Java"))  # Output: 2


sister.index("z") 
# Output: 2
fam.index("mom") 
# Output: 4
# The variable 'place' is a string that stores the word "poolhouse"
place = "poolhouse"

# The .upper() method converts all letters in the string to uppercase.
# It does NOT modify the original string; instead, it returns a new one.
place_up = place.upper()




#Syntax (method call):
#object.method(arguments)
# Print both to compare:
# 'place' remains the same (lowercase)
# 'place_up' is the uppercase version
print(place)      # Output: poolhouse
print(place_up)   # Output: POOLHOUSE

# The .count() method counts how many times a specific character appears in the string.
# Here we count how many 'o' characters are in the variable 'place'
print(place.count("o"))  # Output: 3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Adds "orange" to the end of the list
print(fruits)            # ['apple', 'banana', 'cherry', 'orange']
fruits.remove("banana")  # Removes "banana" from the list
print(fruits)            # ['apple', 'cherry', 'orange']
# Summary:
# .upper() → returns a new uppercase string
# .count('x') → counts occurrences of the letter 'x' in the string
# Strings in Python are immutable, meaning they cannot be changed after creation.





# 🧠 Difference Between Functions and Methods in Python

# 🔹 1. Functions (Independent Built-in Functions)
# Functions are not attached to any specific object.
# You just call them directly and pass the variable as an argument.

numbers = [3, 5, 1, 8]

# max() returns the largest value
print(max(numbers))   # Output: 8

# len() returns the number of elements
print(len(numbers))   # Output: 4

# sorted() returns a new sorted list
print(sorted(numbers))  # Output: [1, 3, 5, 8]


# 🔹 2. Methods (Functions Belonging to Objects)
# Methods are actions that belong to specific data types, like strings or lists.
# You call them using dot notation: object.method()

# Example with a list
numbers.sort()    # sorts the list in place (changes the original)
print(numbers)    # Output: [1, 3, 5, 8]

# Example with a string
text = "hello"
print(text.upper())  # Output: HELLO


# 🔹 3. Quick Summary
# Functions → Standalone, use directly, e.g. max(), len(), sorted()
# Methods → Belong to objects, use dot notation, e.g. .sort(), .upper()


# 🔍 4. Analogy
# A function is like a general tool that can work on anything you give it.
# A method is like a built-in button that works only for a specific object type.
# Understanding this difference helps you know when to use each in your code!


# 🧩 append() vs extend() in Python

# Start with a list of areas
areas = ["hallway", 11.25, "kitchen", 18.0]

# append() adds ONE item at a time
areas.append("poolhouse")
areas.append(24.5)

print(areas)
# Output: ['hallway', 11.25, 'kitchen', 18.0, 'poolhouse', 24.5]

# extend() adds MULTIPLE items at once (more efficient!)
areas.extend(["garage", 15.45])

print(areas)
# Output: ['hallway', 11.25, 'kitchen', 18.0, 'poolhouse', 24.5, 'garage', 15.45]

# 🔹 append() → adds a single element (even if it’s a list)
# 🔹 extend() → adds multiple elements (expands the list)
# len(fam_ext) → counts how many items are in the list "fam_ext"
# str(...) → converts that number to a string (so you can join it with text)
# " elements in fam_ext" → just a text message
# + → combines the number (as a string) with the message
# print(...) → shows the final text on the screen

print(str(len(fam_ext)) + " elements in fam_ext")
# Example output: "12 elements in fam_ext"




#NUMPY 
import numpy as np
import numpy
# Create a 1D NumPy array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)
numpy.array([1,2,3])


from numpy import array 
#if you import only array from numpy, you can use array() directly without the np. prefix.
numpy.array([1,2,3]) #to create a numpy array using the full numpy module name.#it used when you want to avoid namespace conflicts or prefer clarity.
array([1,2,3]) #to create a numpy array using the directly imported array function.

import numpy as np     #to` import the numpy library with the alias np.

fam_ext = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89, "me", 1.79]
# normal list in python

np_fam = np.array(fam_ext)
# to convert the normal list to a numpy array
#it uses the np.array() function from the NumPy library to create a NumPy array called np_fam.
#it used for efficient numerical computations and data manipulation.

print(np_fam)
# to print the numpy array
print(np_fam.dtype)
# to print the data type of the elements in the numpy array 
# Since the original list contains mixed types (strings and floats), the dtype will be 'object'.
# This means the array can hold any type of Python objects.

# 💡 NumPy Arrays in Python
# NumPy arrays are used to store numerical data and perform mathematical operations efficiently.

# ✅ Import the NumPy library (commonly as 'np')
import numpy as np

# ✅ Create a NumPy array
arr = np.array([1, 2, 3])
print(arr)
# Output: [1 2 3]

# ⚙️ Explanation:
# np.array() converts a normal Python list into a NumPy array.
# Arrays are faster and more powerful than Python lists for mathematical operations.

# 🧮 Example: Arithmetic Operations
arr2 = np.array([4, 5, 6])
print(arr + arr2)  # Output: [5 7 9]
print(arr * 2)     # Output: [2 4 6]

# 📏 Example: Basic Statistics
print(arr.mean())  # Output: 2.0
print(arr.sum())   # Output: 6
print(arr.max())   # Output: 3

# 🔍 Difference between list and NumPy array
list1 = [1, 2, 3]
print(list1 + list1)  # Output: [1, 2, 3, 1, 2, 3] (concatenation)
print(arr + arr)      # Output: [2 4 6] (element-wise addition)

# ✅ In summary:
# - np.array() → converts list to array
# - Arrays are faster and support direct math operations
# - Perfect for data science, machine learning, and scientific computing

# Create a 2D NumPy array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array (Matrix):\n", matrix)  # Output:
# [[1 2 3]
#  [4 5 6]]
# Explanation: This is a 2D array (matrix) with 2 rows and 3 columns. #array([[row1], [row2], ...])
# Each inner list represents a row in the matrix. #array([[row1], [row2], ...]) 
# NumPy makes it easy to work with multi-dimensional data. 
# Accessing elements
print("Element at (0,1):", matrix[0, 1])  # Output: 2
# Slicing
print("Sliced Array (1:2, 0:2):\n", matrix[1:2, 0:2]) 
# Output: [[4 5]]
# Basic statistics on the matrix
print("Mean:", matrix.mean())
print("Sum:", matrix.sum())
print("Max:", matrix.max()) 
# Reshaping the array
reshaped = matrix.reshape(3, 2)
print("Reshaped Array (3,2):\n", reshaped) 
# Output: [[1 2]
#          [3 4]
#          [5 6]]
# Explanation: The reshape() method changes the shape of the array without changing its data.
# NumPy arrays are powerful tools for numerical computing in Python!
# They allow for efficient storage and manipulation of large datasets, making them essential for data science and scientific computing tasks.
# Create a NumPy array of integers from 0 to 9
arr = np.arange(10) 
print("Array from 0 to 9:", arr)  # Output: [0 1 2 3 4 5 6 7 8 9] 
# Explanation: np.arange(10) generates numbers from 0 up to (but not including) 10.
# Create a NumPy array of even integers from 0 to 18
even_arr = np.arange(0, 20, 2)
print("Even numbers from 0 to 18:", even_arr)  # Output: [ 0  2  4  6  8 10 12 14 16 18]
# Explanation: np.arange(0, 20, 2) generates numbers from 0 to 19 with a step of 2 (even numbers).
# Create a NumPy array of floating-point numbers from 0.0 to 1.0 with a step of 0.1
float_arr = np.arange(0.0, 1.1, 0.1)
print("Floating-point numbers from 0.0 to 1.0:", float_arr)  # Output: [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1. ]
# Explanation: np.arange(0.0, 1.1, 0.1) generates floating-point numbers from 0.0 to 1.0 with a step of 0.1.

# Generate a NumPy array of integers from 5 to 15
int_arr = np.arange(5, 16)
print("Array from 5 to 15:", int_arr)  # Output: [ 5  6  7  8  9 10 11 12 13 14 15]
# Explanation: np.arange(5, 16) generates numbers from 5 up to (but not including) 16.
# Generate a NumPy array of odd integers from 1 to 19
odd_arr = np.arange(1, 20, 2)   # Output: [ 1  3  5  7  9 11 13 15 17 19]
print("Odd numbers from 1 to 19:", odd_arr)
# Explanation: np.arange(1, 20, 2) generates numbers from 1 to 19 with a step of 2 (odd numbers).
# Generate a NumPy array of floating-point numbers from 0.5 to 2.0 with a step of 0.5
float_arr2 = np.arange(0.5, 2.1, 0.5)
print("Floating-point numbers from 0.5 to 2.0:", float_arr2 )  # Output: [0.5 1.  1.5 2. ]
# Explanation: np.arange(0.5, 2.1, 0.5) generates floating-point numbers from 0.5 to 2.0 with a step of 0.5.        

