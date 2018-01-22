# 	Exercise one
# Print the last item from year and pop
print(year[-1])
print(pop[-1])

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt 

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)

# Display the
plt.show()

# 	Exercise two
# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()

# 	Exercise three
# Import package
import matplotlib.pyplot as plt

# Build Scatter plot
plt.scatter(pop, life_exp)

# Show plot
plt.show()

# 	Exercise four
# Create histogram of life_exp data
plt.hist(life_exp, 10)

# Display histogram
plt.show()

# 	Exercise five
# Histogram of life_exp, 15 bins
plt.hist(life_exp, bins = 15)

# Show and clear plot
plt.show()
plt.clf()

# Histogram of life_exp1950, 15 bins
plt.hist(life_exp1950, bins = 15)

# Show and clear plot again
plt.show()
plt.clf()
