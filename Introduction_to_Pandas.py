# 	Exercise
import pandas
food_info = pandas.read_csv("food_info.csv")

print(food_info)
print(type(food_info))

# 	Exercise
print(food_info.head(3))

dimensions = food_info.shape
print(dimensions)
num_rows = dimensions[0]
print(num_rows)
num_cols = dimensions[1]
print(num_cols)
print(food_info.columns)

first_twenty = food_info.head(20)
print(first_twenty) 

# 	Exercise
# Series object representing the row at index 0.
print(food_info.loc[1])
print(food_info.loc[10])

hundredth_row = food_info.loc[99]
print(hundredth_row)

# 	Exercise
print("Rows 3, 4, 5 and 6")
print(food_info.loc[3:6])

print("Rows 2, 5, and 10")
two_five_ten = [2,5,10]
print(food_info.loc[two_five_ten])

m = food_info.shape
print(m)
index_last_row = m[0]
last_rows = food_info[m[0]-5:m[0]]
print(last_rows)

# 	Exercise
# Series object.
ndb_col = food_info["NDB_No"]
print(ndb_col)

# Display the type of the column to confirm it's a Series object.
print(type(ndb_col))

saturated_fat = food_info["FA_Sat_(g)"]
print(saturated_fat)

cholesterol = food_info["Cholestrl_(mg)"]
print(cholesterol)

# 	Exercise
zinc_copper = food_info[["Zinc_(mg)", "Copper_(mg)"]]

columns = ["Zinc_(mg)", "Copper_(mg)"]
zinc_copper = food_info[columns]
print(zinc_copper)

col = ["Selenium_(mcg)", "Thiamin_(mg)"]
selenium_thiamin = food_info[col]
print(selenium_thiamin)

# 	Exercise
#print(food_info.columns)
#print(food_info.head(2))
col_names = food_info.columns.tolist()
print(col_names)
gram_columns = []

for c in col_names:
    if c.endswith("(g)"):
        gram_columns.append(c)
        print(gram_columns)
        
gram_ft = food_info[gram_columns]
print(gram_ft.head(3))
