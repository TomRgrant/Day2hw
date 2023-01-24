united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
# 3. Use a loop to print the names of all the countries in the UK.
# 4. Use a loop to find the total population of the UK.

#Change Wales capital
united_kingdom[1]["capital"] = "Cardiff"
# print(united_kingdom[1]["capital"])

#Create new location
north_ireland = [{"name": "Northern Ireland",
  "population": "1,811,000",
  "capital": "Belfast",
}]

#Update dict
united_kingdom.append(north_ireland)

# # Loop for all names
# cntr = 0
# for country in united_kingdom:
#   print(united_kingdom[cntr]["name"])
#   cntr += 1

# #Loop for total population
# cntr = 0
# total_pop = 0
# for country in united_kingdom:
#   total_pop += united_kingdom[cntr]["population"]
#   cntr += 1

# #print the total pop
# print(f"{total_pop} Is the population of all countries")
