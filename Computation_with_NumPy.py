# 	Exercise
countries_canada = (world_alcohol[:,2] == "Canada") 

years_1984 =  (world_alcohol[:,0] == "1984") 
print(years_1984)

# 	Exercise
vector = numpy.array([5, 10, 15, 20])
equal_to_ten = (vector == 10)

print(equal_to_ten)
print(vector[equal_to_ten])

country_is_algeria = (world_alcohol[:,2] == "Algeria")
country_algeria = world_alcohol[country_is_algeria]

print(country_algeria)
print(country_is_algeria)

# 	Exercise
is_algeria_and_1986 = (world_alcohol[:,0] == "1986") & ( world_alcohol[:,2] == "Algeria")
print(is_algeria_and_1986)

rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986] 
print(rows_with_algeria_and_1986)

# 	Exercise
vector = (world_alcohol[:,0] == "1986")
print(vector)

world_alcohol[vector,0] = "2014"
print(world_alcohol)

vector = (world_alcohol[:,3] == "Wine")
print(vector)

world_alcohol[vector,3] = "Grog"
print(world_alcohol)

# 	Exercise
is_value_empty = (world_alcohol[:, 4] == "")

print(is_value_empty)
world_alcohol[is_value_empty, 4] = 0 

# 	Exercise
alcohol_consumption = world_alcohol[:,4]
print(alcohol_consumption)

alcohol_consumption = alcohol_consumption.astype(float)
print(alcohol_consumption)

# 	Exercise
total_alcohol = alcohol_consumption.sum() 
print(total_alcohol)

average_alcohol = alcohol_consumption.mean()

# 	Exercise
is_canada_1986 = (world_alcohol[:,2] == "Canada") & (world_alcohol[:,0] == '1986')
canada_1986 = world_alcohol[is_canada_1986,:]
canada_alcohol = canada_1986[:,4]

f = canada_alcohol == ''
canada_alcohol[f] = "0"

canada_alcohol = canada_alcohol.astype(float)
total_canadian_drinking = canada_alcohol.sum()

# 	Exercise
totals = {}
is_year = world_alcohol[:,0] == "1989"
year = world_alcohol[is_year,:] 

print(year)

for country in countries:
    i = year[:, 2] == country
    jes = year[i, 4]
    emply_jes = jes == ""
    jes[emply_jes] = "0"
    jes = jes.astype(float)
    totals[country] = jes.sum()

# 	Exercise
highest_value = 0
highest_key = None

is_year = world_alcohol[:,0] == "1989"
year = world_alcohol[is_year,:] 

print(year)

for country in countries:
    i = year[:, 2] == country
    jes = year[i, 4]
    emply_jes = jes == ""
    jes[emply_jes] = "0"
    jes = jes.astype(float)
    totals_sum_country = jes.sum()
    if (totals_sum_country > highest_value):
        highest_value = totals_sum_country
        highest_key = country

        print("************")
        print(totals_sum_country)
        print(country)
        print("************")