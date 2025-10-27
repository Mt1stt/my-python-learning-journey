#lists=[]
# list can contain a mix of Python types including strings, floats, and booleans.
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

#instead of putting ever element in variable like x1 = "apple" x2 = "banana" x3 = "cherry"
#do it 
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[-1])  # cherry
fruits[1] = 42
# now: ["apple", 42, "cherry"]
print(fruits)
print(fruits[-1])
print(fruits[0:2])
print(fruits[:2])
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])
#Use slicing to create a list, downstairs, that contains the first 6 elements of areas.
#Create upstairs, as the last 4 elements of areas. This time, simplify the slicing by omitting the end index.
#Print both downstairs and upstairs using print().

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[-4:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)



house = [
    ["hallway", 11.25],
    ["kitchen", 18.0],
    ["living room", 20.0],
    ["bedroom", 10.75],
    ["bathroom", 9.50]
]
#Each inner list contains:The room name The area (float number)
#So for "bathroom", the float 9.50 is the second item (index 1) inside the last list (index 4).
# How to subset (get 9.5) You need two levels of indexing:

house[4][1]

#house[4] → gives ["bathroom", 9.50] house[4][1] → gives the second value inside it → 9.50

print(house[4][1])

#PREVIOUS WAS LIST,SUBSETTING LIST 
#MANIPULATION 
# -----------------------------------------------
# 🧠 Behind the scenes (1)
# When you assign y = x, Python does NOT create a new list.
# Instead, both x and y point to the SAME list in memory.
#
# That means: if you change something in y, 
# it will also affect x because they share the same reference.
# -----------------------------------------------

# Create a list and store it in variable x
x = ["a", "b", "c"]

# Assign y to the same list as x (no copy is made)
y = x

# Change the second element of y to "z"
y[1] = "z"

# Print y
print(y)  # Output: ['a', 'z', 'c']

# Print x
print(x)  # Output: ['a', 'z', 'c']

# -----------------------------------------------
# 🧠 Behind the scenes (2)
# In this example, we create a *copy* of the list.
#
# When we write y = list(x) or y = x[:],
# Python makes a NEW list in memory with the same elements as x.
#
# That means: if we change y, x will NOT be affected anymore,
# because they now point to two separate lists.
# -----------------------------------------------

# Create a list
x = ["a", "b", "c"]

# Make a copy of x
y = list(x)  # or y = x[:]

# Change one element in y
y[1] = "z"

# Print both lists
print("x =", x)  # ['a', 'b', 'c'] (unchanged)
print("y =", y)  # ['a', 'z', 'c'] (only y changed)


#dipendency between lists 
# -----------------------------------------------
# 🧠 Replacing elements inside a list
# There are two main cases:
# -----------------------------------------------

# 🟢 1. Simple list
# If you have a normal list with numbers or values,
# you can replace an element directly using its index.
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Replace the last element using a negative index
areas[-1] = 10.50

print(areas)
# Output: [11.25, 18.0, 20.0, 10.75, 10.50]

# -----------------------------------------------

# 🔵 2. List of lists
# If you have a list that contains other lists (nested list),
# you must use TWO indices:
#   - The first one selects the sublist
#   - The second one selects the element inside that sublist
house = [
    ["hallway", 11.25],
    ["kitchen", 18.0],
    ["living room", 20.0],
    ["bedroom", 10.75],
    ["bathroom", 9.50]
]

# Replace the area of the bathroom (the 2nd value in the 5th list)
house[4][1] = 10.50

print(house)
# Output: ['bathroom', 10.50] as part of the last sublist

# -----------------------------------------------
# 💡 Summary:
# - areas[-1] = 10.50 → works with a simple list
# - house[4][1] = 10.50 → works with a list of lists
# -----------------------------------------------
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50
# Change "living room" to "chill zone"
areas[4]="chill zone"


