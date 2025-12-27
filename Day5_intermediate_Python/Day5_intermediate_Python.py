import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt


# plt.plot() → Draws a line plot (Line chart)

# plt.scatter() → Draws a scatter plot (Points)

# plt.bar() → Draws a bar chart (Bars)

# plt.hist() → Draws a histogram (Data distribution)

# plt.pie() → Draws a pie chart (Circle chart)

# plt.boxplot() → Draws a box plot (Shows data spread)

# plt.imshow() → Displays data as a heatmap (Colors)

# plt.fill_between() → Draws an area plot (Filled area under line)

# Subplots → Draws multiple plots in one figure

# Axes3D → Used for 3D plots (x, y, z)

# plt.show() → Displays the plot on the screen

# plt.clf() → Clears the current figure like a whiteboard and gets it ready for the next plot and plt.close() → Closes the figure window


# Simple line plot
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()

# Population over the years
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
plt.plot(year, pop)
plt.show()

# Scatter plot example
years = [1950, 1970, 1990, 2010]
populations = [2.519, 3.692, 5.263, 6.972]
plt.scatter(years, populations) 
plt.show()

# Bar chart example
years = [1950, 1970, 1990, 2010]                
populations = [2.519, 3.692, 5.263, 6.972]
plt.bar(years, populations)
plt.show()

# Histogram example
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.hist(data, bins=4)          
plt.show()

# Pie chart example
labels = ['A', 'B', 'C', 'D']   
sizes = [15, 30, 45, 10]
plt.pie(sizes, labels=labels)
plt.show()

# Customized line plot
x = [1, 2, 3, 4, 5] 
y = [2, 3, 5, 7, 11]
plt.plot(x, y, color='green', linestyle='--', marker='o', markerfacecolor='blue', markersize=8)
plt.title('Customized Line Plot')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')  
plt.grid(True)
plt.show()

# Multiple lines in one plot
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]   
plt.plot(x, y1, label='Line 1', color='blue')
plt.plot(x, y2, label='Line 2', color='red')
plt.title('Multiple Lines Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()

# Subplots example
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(x, y1, color='blue')
ax1.set_title('First Subplot')
ax2.plot(x, y2, color='red')
ax2.set_title('Second Subplot')
plt.tight_layout()
plt.show()
# Saving a plot to a file
x = [1, 2, 3, 4, 5] 
y = [2, 3, 5, 7, 11]
plt.plot(x, y)
plt.title('Plot to be Saved')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.savefig('saved_plot.png')
plt.close()
# Creating a figure with multiple subplots in a grid
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# First subplot
axes[0, 0].plot([1, 2, 3], [1, 4, 9], color='blue')
axes[0, 0].set_title('Square Numbers')

# Second subplot
axes[0, 1].scatter([1, 2, 3, 4], [2, 4, 6, 8], color='red')
axes[0, 1].set_title('Linear Data')

# Third subplot
axes[1, 0].bar(['A', 'B', 'C'], [10, 24, 36], color='green')
axes[1, 0].set_title('Bar Chart')

# Fourth subplot
axes[1, 1].hist([1, 1, 2, 2, 2, 3, 3, 3, 3, 4], bins=4, color='orange')
axes[1, 1].set_title('Distribution')

plt.tight_layout()
plt.show()
# Line plot with annotations
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x, y, marker='o')
plt.title('Line Plot with Annotations')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add annotations to each point
for i, j in zip(x, y):
    plt.annotate(str(j), xy=(i, j), xytext=(5, 5), textcoords='offset points')

plt.show()
# Box plot example
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6]
plt.boxplot(data)
plt.title('Box Plot')
plt.ylabel('Values')
plt.show()

# Heatmap example
data = np.random.rand(5, 5)
plt.imshow(data, cmap='hot')
plt.colorbar()
plt.title('Heatmap')
plt.show()

# Area plot example
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.fill_between(x, y, alpha=0.5)
plt.plot(x, y, marker='o')
plt.title('Area Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# 3D scatter plot example
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
z = [1, 4, 6, 8, 10]
ax.scatter(x, y, z)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
plt.show()


###########################################################################

# Change the line plot below to a scatter plot

gdp_cap = [400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0]
life_exp = [70.0, 71.5, 72.0, 73.0, 74.0, 75.0, 76.0]
plt.plot(gdp_cap, life_exp)
plt.xscale('log')   
plt.show()

# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)  
# Put the x-axis on a logarithmic scale
plt.xscale('log')   
# Show plot
plt.show()

# Import package
import matplotlib.pyplot as plt
# Build Scatter plot
plt.scatter(pop,life_exp)
# Show plot
plt.show()


#############################################################################################################################

#histogram plot
import matplotlib.pyplot as plt
pop = [2.519, 3.692, 5.263, 6.972, 7.593, 8.051, 8.547, 9.216, 9.771, 10.079]
plt.hist(pop, bins=5)
plt.show()
# Modify the histogram to use 5 bins instead of 10
plt.hist(pop, bins=5)
plt.show()  

#but Scatter plot The relationship between two variables
# Line plot → For time, the horizontal axis represents time (year, day, month). We see the change over time. Example: Population from 1950 to 2020.
# Histogram → Not for time, the horizontal axis represents values ​​divided into categories whose chronological order is not important. We see the distribution. Example: Exam scores, ages of people, heights of students.

#################################################################################################################################################################################################
#customization in matplotlib
import matplotlib.pyplot as plt 
year = [1950, 1951, 1952,..., 2100]  # Example years from 1950 to 2100
pop = [2.519, 2.556, 2.594,..., 10.079]  # Corresponding population values

#add more data
year = [1850, 1970, 1990, 2010] + year
pop = [1.262, 3.692, 5.263, 6.972] + pop
plt.plot(year, pop, color='green', linestyle='--', marker='o', markerfacecolor='blue', markersize=8)
plt.title('World Population Growth')
plt.xlabel('Year')
plt.ylabel('Population')

plt.yticks([0, 2, 4, 6, 8, 10, 12],['0b', '2b', '4b', '6b', '8b', '10b', '12b'])

plt.grid(True)
plt.show()
# Change the line color to red, the line style to dotted, and add square markers
plt.plot(x, y, color='red', linestyle=':', marker='s', markerfacecolor='blue', markersize=8)
plt.title('Customized Line Plot')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.grid(True)
plt.show()

# plt.xscale() is used to change the scale of the X-axis

# Default scale is 'linear'
# Linear scale means numbers increase normally (1, 2, 3, 4)

# plt.xscale('log') sets the X-axis to logarithmic scale
# Log scale is useful when values are very large

# Log scale helps spread data points
# It makes relationships clearer when numbers vary a lot

# Important: plt.xscale() changes how data is displayed
# It does NOT change the actual data values



#tick_val, tick_lab  = [1000, 10000, 100000, 1000000], ['1k', '10k', '100k', '1M'] . vla used for setting the ticks on x axis . lab used for labelling the ticks on x axis
#example # Scatter plot
plt.scatter(gdp_cap, life_exp)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xlabel('tick_val')
plt.xlabel('tick_lab')

# After customizing, display the plot
plt.xticks(tick_val, tick_lab)
plt.show()

#example ##################################

#Exercise: Sizes Right now, the scatter plot is just a cloud of blue dots, indistinguishable from each other. Let's change this. Wouldn't it be nice if the size of the dots corresponds to the population? To accomplish this, there is a list pop loaded in your workspace. It contains population numbers for each country expressed in millions. You can see that this list is added to the scatter method, as the argument s, for size. Run the script to see how the plot changes. Looks good, but increasing the size of the bubbles will make things stand out more. Import the numpy package as np. Use np.array() to create a numpy array from the list pop. Call this NumPy array np_pop. Double the values in np_pop setting the value of np_pop equal to np_pop * 2. Because np_pop is a NumPy array, each array element will be doubled. Change the s argument inside plt.scatter() to be np_pop instead of pop.

# Import numpy as np
import numpy as np

# Store pop as a numpy array: np_pop
np_pop=np.array(pop)

# Double np_pop
np_pop = np_pop * 2


# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()

#we used s argument to set the size of the scatter plot points according to population 

plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)
# Here, we set the size (s) of each point to be proportional to the population (pop) multiplied by 2 for better visibility.
# We also set the color (c) of each point to be determined by the col list
# The alpha parameter controls the transparency of the points, with 0 being fully transparent and 1 being fully opaque.
