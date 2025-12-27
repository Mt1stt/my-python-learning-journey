#it uses indentation to define code blocks.and it is case-sensitive.
#what is package in python?
#A package in Python is a way to organize related modules into a directory structure, allowing for better code management and reuse. 
#Packages contain an __init__.py file and can include sub-packages and modules.
#example of package: numpy, pandas, matplotlib, requests, etc.
#Numpy is a powerful library in Python used for numerical computing. It provides support for arrays, matrices, and a wide range of mathematical functions to operate on these data structures efficiently.
#Numpy is widely used in data science, machine learning, and scientific computing due to its
#ability to handle large datasets and perform complex calculations quickly.
#mod1ule1.py
import numpy as np
# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)
# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)
# Perform basic operations
sum_array = np.sum(array_1d)
print("Sum of 1D Array:", sum_array)
mean_array = np.mean(array_2d)
print("Mean of 2D Array:", mean_array)
# Reshape an array
reshaped_array = array_1d.reshape((5, 1))
print("Reshaped Array:\n", reshaped_array)

# Import the math package
import math

# Calculate C
C = 2 * 0.43 * math.pi

# Calculate A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C)) 
print("Area: " + str(A)) 

from scipy.linalg import inv as my_inv
import numpy as np

# Matrix 2x2
A = np.array([[1, 2], [3, 4]])

# CALCULATE Inverse
A_inv = my_inv(A)

print("Original Matrix:\n", A)
print("Inverse Matrix:\n", A_inv)


#another war 
import numpy as np

A = np.array([[1, 2], [3, 4]])
A_inv = np.linalg.inv(A)
print(A_inv)

#Which command explicitly imports the function sort()from the package numpy? Select the correct answer
#from numpy import sort


height=[1.73, 1.68, 1.71, 1.89, 1.79]
weight=[65.4, 59.2, 63.6, 88.4, 68.7] 
import numpy as np 
np_height = np.array(height)
np_weight = np.array(weight)    
bmi = np_weight / np_height ** 2
print(bmi)
#but numpy arrays contains only one type of elements 

#notes 
#np.array([True, 1, 2]) + np.array([3, 4, False]) =  np.array([4, 3, 0]) + np.array([0, 2, 2])
#
# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)

#
# Import the numpy package as np
import numpy as np

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball=np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball)) 
print(np_baseball.shape)  #(8,) 1D array with 8 elements 


import numpy as np

bmi = np.array([21.85171573, 20.97505669, 21.75028214, 24.7473475, 21.44127836])

print(bmi[1])

print(bmi > 23)


import numpy as np

np_weight_lb = np.array(weight)
np_height_in = np.array(height)

# Print out the weight at index 50
print(np_weight_lb[4])

# Print out sub-array of np_height_in: index 1 up to and including index 3
sub_array = np_height_in[1:4] 

print(sub_array)
import numpy as np

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])

np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

type(np_height) #numpy.ndarray

type(np_weight) #numpy.ndarray #is a multidimensional array object used to store elements of the same data type.

#If you ask for the type of these arrays, Python tells you that they are numpy.ndarray. numpy dot tells you it's a type that was defined in the numpy package. ndarray stands for n-dimensional array. The arrays np_height and np_weight are one-dimensional arrays, but it's perfectly possible to create 2 dimensional, three dimensional, heck even seven dimensional arrays! Let's see how we can use these arrays to do some calculations.
bmi = np_weight / np_height ** 2
print(bmi)
#The expression np_height ** 2 takes each element of the array np_height and squares it. The result is a new array with the squared values. Then, np_weight / np_height ** 2 divides each element of the array np_weight by the corresponding element of the squared np_height array. The result is another new array containing the BMI values for each individual.
#This is called element-wise operations, and it's one of the most powerful features of numpy arrays. It allows you to perform mathematical operations on entire arrays without the need for explicit loops, making your code more concise and efficient. 
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])   
bmi = np_weight / np_height ** 2
print(bmi)
# Output: [21.85171573 20.97505669 21.75028214 24.7473475  21.44127836]
#This will output the BMI values for each individual in the arrays.
#Numpy arrays are more efficient than regular Python lists for numerical computations because they are implemented in C and optimized for performance. They use less memory and allow for faster operations due to their contiguous memory allocation and ability to perform vectorized operations.
#In contrast, Python lists are more flexible and can hold elements of different data types, but
#they are less efficient for numerical computations due to their dynamic nature and the overhead of storing type information for each element.
#Numpy arrays are designed to handle large datasets and perform complex mathematical operations efficiently, making them a preferred choice for data science and scientific computing tasks.
#Numpy arrays are more efficient than regular Python lists for numerical computations because they are implemented in C and optimized for performance. They use less memory and allow for faster operations due to their contiguous memory allocation and ability to perform vectorized operations.
#In contrast, Python lists are more flexible and can hold elements of different data types, but
#they are less efficient for numerical computations due to their dynamic nature and the overhead of storing type
#information for each element.
#Numpy arrays are designed to handle large datasets and perform complex mathematical operations efficiently, making them
#a preferred choice for data science and scientific computing tasks.


np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],

[ 65.4, 59.2, 63.6, 88.4,

68.7]])

print(np_2d) #array([[ 1.73,1.68,1.71,1.89,1.79],[65.4 59.2 63.6 88.4 68.7 ]])

print(np_2d.shape)  #(2, 5)          # 2 rows, 5 columns
#The shape attribute of a numpy array returns a tuple representing the dimensions of the array. In this case, np_2d has 2 rows and 5 columns, so its shape is (2, 5).
print(np_2d[0])    #array([1.73, 1.68, 1.71, 1.89, 1.79])  #first row
print(np_2d[1])    #array([65.4, 59.2, 63.6, 88.4, 68.7])   #second row
print(np_2d[:,0])  #array([ 1.73, 65.4])               #first column
print(np_2d[:,1])  #array([ 1.68, 59.2])               #second column           
print(np_2d[0,2])  #1.71                             #element at first row, third column
print(np_2d[1,3])  #88.4                             #element at second row, fourth column
#In numpy, you can access elements of a 2D array using indexing. The syntax for accessing elements is array[row_index, column_index]. You can also use slicing to access entire rows or columns.
#For example, np_2d[0] accesses the first row of the array, while np_2d[:,0] accesses the first column. You can also access individual elements by specifying both the row and column indices, such as np_2d[0,2] for the element in the first row and third column.        
import numpy as np  
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
[65.4, 59.2, 63.6, 88.4, 68.7]])
bmi = np_2d[1, :] / np_2d[0, :] ** 2
print(bmi)  
# Output: [21.85171573 20.97505669 21.75028214 24.7473475  21.44127836]
#In this example, np_2d[1, :] accesses the second row (weights) and np_2d[0, :] accesses the first row (heights). The BMI is calculated by dividing the weights by the square of the heights, resulting in an array of BMI values for each individual.  
np_2d = [
[1.73, 1.68, 1.71, 1.89, 1.79],   #← row 0
[65.4, 59.2, 63.6, 88.4, 68.7]    #← row 1
]
print(np_2d[0][2])  #1.71  ← element at row 0, column 2
print(np_2d[1][3])  #88.4  ← element at row 1, column 3
#In this example, np_2d[0][2] accesses the element in the first row (row index 0) and third column (column index 2), which is 1.71. Similarly, np_2d[1][3] accesses the element in the second row (row index 1) and fourth column (column index 3), which is 88.4.
#This method of indexing is similar to how you would access elements in a list of lists in
np_2d[:, 1:3]
#array([[1.68, 1.71],
#       [59.2, 63.6]])
#In this example, np_2d[:, 1:3] uses slicing to access all rows (indicated by :) and columns 1 to 2 (the end index 3 is exclusive). The result is a new array containing the specified columns from all rows.
np_2d[1, :]
#array([65.4, 59.2, 63.6, 88.4, 68.7])
#In this example, np_2d[1, :] accesses the second row (row index 1) and all columns (indicated by :). The result is a new array containing all the weights from the second row. 
#2D numpy arrays enable you to do element-wise calculations, the same way you did it with 1D numpy arrays. For example, you can calculate the BMI for each individual in the 2D array by dividing the weights by the square of the heights.


#EXAMPLE import numpy as np
#Print out the 50th row of np_baseball.
#Make a new variable, np_weight_lb, containing the entire second column of np_baseball.
#Select the height (first column) of the 124th baseball player in np_baseball and print it out.
#np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
#print(np_baseball[49, :])

# Select the entire second column of np_baseball: np_weight_lb
#np_weight_lb = np_baseball[:, 1]

# Print out height of 124th player
#print(np_baseball[123,:])

#NOTICE THE (,) IN THE SHAPE OUTPUT AND [,] IN THE INDEXING OUTPUT AND (:) IN THE SLICING OUTPUT AND HOW THEY DIFFER FROM EACH OTHER 1D AND 2D ARRAYS   1D ARRAY HAS ONLY ONE ROW OR ONE COLUMN BUT 2D ARRAY HAS MULTIPLE ROWS AND COLUMNS 1D ARRAY SHAPE OUTPUT HAS ONLY ONE VALUE IN THE TUPLE LIKE (8,) BUT 2D ARRAY SHAPE OUTPUT HAS TWO VALUES IN THE TUPLE LIKE (2,5) 1D ARRAY INDEXING OUTPUT HAS ONLY ONE VALUE LIKE [4] BUT 2D ARRAY INDEXING OUTPUT HAS TWO VALUES LIKE [1,3] 1D ARRAY SLICING OUTPUT HAS ONLY ONE COLON LIKE [1:4] BUT 2D ARRAY SLICING OUTPUT HAS TWO COLONS LIKE [:,1:3]


#example ##import numpy for array operations
#import numpy as np

#convert the baseball list into a 2D numpy array
#np_baseball = np.array(baseball)

#add the updated changes to the original data
#print(np_baseball + updated)   #adds height, weight, and age changes element-wise

#create a conversion array for height (in→m), weight (lb→kg), and age (no change)
#conversion = np.array([0.0254, 0.453592, 1])   #1 keeps age unchanged

#multiply the baseball data by the conversion factors
#print(np_baseball * conversion)   #converts all measurements to metric units


#to calculate mean and median of a column in 2D numpy array
#import numpy as np 
#np.mean(np_city[:, 0]) #1.7472
#np.median(np_city[:, 0]) #1.75

#to calculate correlation and standard deviation of columns in 2D numpy array
#np.corrcoef(np_city(:, 0], np_city[:, 1])

#array([[ 1.-0.01802],
#[-0.01803, 1.]])
#np.std(np_city[:, 0]) #0.1992
#sum(), sort(), ... #Enforce single data type: speed!
#Element-wise operations: fast!
#Multidimensional arrays


#To generate random data for height and weight using NumPy, you can use the np.random.normal() function, which generates samples from a normal (Gaussian) distribution. Here's how you can do it:
#Generate data
#Arguments for np.random.normal()
#distribution mean
#distribution standard deviation
#number of samples

#height = np.round(np.random.normal(1.75, 0.20, 5000), 2)

#weight = np.round(np.random.normal(60.32, 15, 5000), 2)

#np_city = np.column_stack((height, weight))
## Explanation:
# np.random.normal(1.75, 0.20, 5000) generates 5000 samples of height data with a mean of 1.75 meters and a standard deviation of 0.20 meters.
# np.random.normal(60.32, 15, 5000) generates 5000 samples of weight data with a mean of 60.32 kg and a standard deviation of 15 kg.
# np.round(..., 2) rounds the generated data to 2 decimal places for better readability.
# np.column_stack((height, weight)) combines the height and weight arrays into a single 2D array where each row represents a person with their height and weight.   
#the resulting np_city array will have 5000 rows and 2 columns (height and weight).
#this data can be used for various analyses, such as statistical analysis, machine learning, or data visualization.
#THEN YOU CAN USE THE FOLLOWING CODE:
# Print the first 10 rows of the array  
#print(np_city[:10]) # Output: first 10 rows of height and weight data







#example
#avg = np.mean(np_baseball[:,0])
#print("Average: " + str(avg))

# Print median height
#med = np.median(np_baseball[:,0])
#print("Median: " + str(med))

# Print out the standard deviation on height
#stddev = np.std(np_baseball[:,0])
#print("Standard Deviation: " + str(stddev))
    
# Print out correlation between first and second column
#corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
#print("Correlation: " + str(corr))