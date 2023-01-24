users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
# 2. Get Erik's hometown
# 3. Get the list of Erik's lottery numbers
# 4. Get the species of Avril's pet Monty
# 5. Get the smallest of Erik's lottery numbers
# 6. Return an list of Avril's lottery numbers that are even
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
# 8. Change Erik's hometown to Edinburgh
# 9. Add a pet dog to Erik called "fluffy"
# 10. Add another person to the users dictionary


print(users["Jonathan"]["twitter"])
print(users["Erik"]["home_town"])
print(users["Erik"]["lottery_numbers"])
print(users["Avril"]["pets"][0])
print(min(users["Erik"]["lottery_numbers"]))

#Get even lotto nums for Avril
even_lotto = []
for num in users["Avril"]["lottery_numbers"]:
  if num % 2 == 0:
    even_lotto.append(num)

print(even_lotto)

#Add 7 to Erik's lotto nums
users["Erik"]["lottery_numbers"].append(7)
print(users["Erik"]["lottery_numbers"])

#Change Eriks home town
users["Erik"]["home_town"] = "Edinburgh"
print(users["Erik"]["home_town"])

#Add dog named fluffy to Erik
# users["Erik"]["pets"] += {"name": "fluffy", "species": "dog"}
# add_fluffy = {"name": "fluffy", "species": "dog"}
users["Erik"]["pets"].append({"name": "fluffy", "species": "dog"})
print(users["Erik"]["pets"])

#Add new user
users[-1] = "Tom",{
    "twitter": "TomTwit",
    "lottery_numbers": [7, 14, 21, 28, 35, 42],
    "home_town": "Aberdeen",
    "pets": [
      {
        "name": "frank",
        "species": "frog"
      }
    ]
  },
      
print(users)




