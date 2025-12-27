print(4+3)
x=4 #variables
y=3
print(x+y)
height=1.79
weight=90
BMI=weight/height**2
print(BMI)
print(type(y))
monthly_savings=10 
num_months=4
new_savings=monthly_savings * num_months
print(new_savings)
savings = 100
new_savings = 40

# Calculate total_savings using savings and new_savings
total_savings = savings + new_savings
print(total_savings)

# Print the type of total_savings
print(type(total_savings))


# Ask the user to enter their name
name = input("What's your name? ")

# Greet the user using the name they typed
print("Hello,", name, "! Welcome to Python learning!")
age = input("How old are you? ")
print("You are", age, "years old.") 
height = input("Enter your height in meters: ")
height = float(height)  # Convert the input string to a float
weight = input("Enter your weight in kilograms: ")
weight = float(weight)  # Convert the input string to a float   
bmi = weight / height**2
print("Your BMI is:", bmi)



#Python #fStrings #FormattedStringLiteral #VariablesInStrings #CodingTips #LearnPython #Programming #PythonTips #CodeClean #DevTips #PythonCoding #TechTips

name = "Ali"
print(f"Hello, {name}!")  # Output: Hello, Ali!

#Without f-string
print("Hello, {name}!")  # Output: Hello, {name}!


#Data types is : int, float, str, bool, numpy 
