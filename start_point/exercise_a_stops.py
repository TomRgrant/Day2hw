stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
#2. Add "Glasgow Queen St" to the start of the list
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
#4. Print out the index position of "Linlithgow"
#5. Remove "Livingston" from the list using its name
#6. Delete "Cumbernauld" from the list by index
#7. Print the number of stops there are in the list
#8. Sort the list alphabetically
#9. Reverse the positions of the stops in the list
#10 Print out all the stops using a for loop



# PythonMethods
# https://docs.python.org/3/tutorial/datastructures.html
# quiz
# https://docs.google.com/forms/d/e/1FAIpQLSc0FNd66FGGdtQMRC6_fx5r3mp6zGA3EP2e1VoImdqS2FcAiA/viewform

#Add new stops
stops.append("Edinvurgh Waverly")
stops.insert(0 ,"Glasgow Queen St")
stops.insert(4, "Polmont")

#Print the index value of Linlithgow
print(stops.index("Linlithgow"))

#Remove Livingston from list
stops.remove("Livingston")

#Deletes Cumbernauld
del stops[2]

#Find how many stops
stops_total = len(stops)

#Print total stops
print(stops_total)

#Sort list aphalbetically
sorted_stops = sorted(stops)
sorted_stops.sort(reverse=True)

#Print out all stops using for loop
counter = 0
for stop in stops:
    print(stops[counter])
    counter += 1