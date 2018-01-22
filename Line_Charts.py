# 	Exercise
import pandas as pd
unrate = pandas.read_csv("unrate.csv")
print(unrate)

unrate['DATE'] = pd.to_datetime(unrate['DATE'])
print(unrate.head(12))

# 	Exercise
first_twelve = unrate[0:12]
plt.plot(first_twelve['DATE'], first_twelve['VALUE'])
plt.show()

# 	Exercise
plt.plot(first_twelve['DATE'], first_twelve['VALUE'])
plt.xticks(rotation=90)
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends, 1948')
plt.show()