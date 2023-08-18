import pandas as pd

data = [
{"Country": "USA", "Population": 328200000, "GDP": 21439400, "Unemployment": 3.8},
{"Country": "China", "Population": 1393000000, "GDP": 14342920, "Unemployment": 3.6},
{"Country": "Japan", "Population": 126500000, "GDP": 5082465, "Unemployment": 2.4},
{"Country": "Germany", "Population": 82790000, "GDP": 3845481, "Unemployment": 3.4},
{"Country": "India", "Population": 1354000000, "GDP": 2956756, "Unemployment": 6.1},
{"Country": "France", "Population": 66990000, "GDP": 2930535, "Unemployment": 8.0},
{"Country": "United Kingdom", "Population": 66440000, "GDP": 2825208, "Unemployment": 4.1},
{"Country": "Italy", "Population": 60480000, "GDP": 2086911, "Unemployment": 9.9},
{"Country": "Brazil", "Population": 209300000, "GDP": 1868626, "Unemployment": 11.6},
{"Country": "Canada", "Population": 37590000, "GDP": 1673625, "Unemployment": 5.6},
{"Country": "South Korea", "Population": 51310000, "GDP": 1660119, "Unemployment": 3.9},
{"Country": "Australia", "Population": 25200000, "GDP": 1403313, "Unemployment": 5.2},
{"Country": "Russia", "Population": 144500000, "GDP": 1402081, "Unemployment": 4.8},
{"Country": "Spain", "Population": 46560000, "GDP": 1394215, "Unemployment": 14.1},
{"Country": "Mexico", "Population": 126200000, "GDP": 1212294, "Unemployment": 3.3},
{"Country": "Indonesia", "Population": 267700000, "GDP": 1075216, "Unemployment": 5.3},
{"Country": "Netherlands", "Population": 17430000, "GDP": 909887, "Unemployment": 3.6},
{"Country": "Saudi Arabia", "Population": 33699947, "GDP": 793697, "Unemployment": 12.9},
{"Country": "Turkey", "Population": 82003882, "GDP": 754605, "Unemployment": 11.1},
{"Country": "Switzerland", "Population": 8541000, "GDP": 703080, "Unemployment": 2.6},
{"Country": "Nigeria", "Population": 214000000, "GDP": 448120, "Unemployment": 23.1},
]

country_data = pd.DataFrame(data)

country_data

print('My name is Funmilayo, and here are my answers: ')

# 1. Which country has the highest population?

data_country_population = country_data.loc[country_data['Population'].idxmax(),'Country']

print('1. Country with the highest poulation : ', data_country_population)

# 2. What is the average GDP across all countries?

data_country_gdp = country_data['GDP'].mean()

print('2. Average GDP across all countries : ', data_country_gdp)

# 3. Which country has the lowest unemployment rate?

data_country_unemployment = country_data.loc[country_data['Unemployment'].idxmin(),'Country']

print('3. Country with the lowest uneemployment rate : ',data_country_unemployment)

# 4. What is the total population of the top 5 countries by GDP?

total_popu_GDP = country_data.sort_values(['GDP'],ascending = [False]).head(5)

total_popu_GDP

sum_population = total_popu_GDP['Population'].sum()

print('4. Total population of the top 5 countries by GDP :' ,sum_population)

# 5.  How many countries have a GDP higher than 5 million?

country_higher = (country_data['GDP'] > 5000000).sum()

print('5. Number of countries with GDP higher than 5 million : ', country_higher)

# 6. Which country has the lowest GDP per capita?

country_lowest = country_data.loc[country_data['GDP'].idxmin(),'Country']

print('6. Country with the lowest GDP per capita :' , country_lowest)

