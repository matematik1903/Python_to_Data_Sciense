# 	Exercise
import numpy as np

vector = np.array([10, 20, 30])
matrix = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]]) 

# 	Exercise
import numpy as np

vector = np.array([10, 20, 30])
matrix = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

vector_shape = vector.shape
matrix_shape = matrix.shape

print(vector_shape)
print(matrix_shape)

# 	Exercise
world_alcohol_dtype = world_alcohol.dtype
print(world_alcohol_dtype)

# 	Exercise
import numpy
world_alcohol = numpy.genfromtxt("world_alcohol.csv", delimiter=",")
print(type(world_alcohol))

# 	Exercise
world_alcohol = np.genfromtxt("world_alcohol.csv", delimiter=",", dtype="U75", skip_header=1)
print(world_alcohol)

# 	Exercise
uruguay_other_1986 = world_alcohol[1, 4]
third_country = world_alcohol[2, 2]

print(third_country)
print(uruguay_other_1986)

# 	Exercise
countries = world_alcohol[:,2]
alcohol_consumption = world_alcohol[:,4]

# 	Exercise
first_two_columns = world_alcohol[:,:2] 
first_ten_years = world_alcohol[:10,0]
first_ten_rows = world_alcohol[:10,:]

# 	Exercise
first_twenty_regions = world_alcohol[0:20,1:3]