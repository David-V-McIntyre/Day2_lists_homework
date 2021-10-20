stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]
print(stops)
print("This is the list with no alterations")
print(" ")
#1. Add "Edinburgh Waverley" to the end of the list
stops.append("Edinburgh Waverley")
print(stops)
print("this is the list of stops with waverley added!")
print(" ")
#2. Add "Glasgow Queen St" to the start of the list
stops.insert(0, "Glasgow Queen St")
print(stops)
print("this is the list of stops with GSQ added!")
print(" " )
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.insert(4, "Polmont")
print(stops)
print("this is the list of stops with Polmont added between Falkirk High and Linlithgow!")
print(" ")
#4. Print out the index position of "Linlithgow"
item = "Linlithgow"
index = stops.index(item)
print(index)
print("this is supposed to be the index position of Linlithgow!")
print(" ")
# very very stuck on how to do this
#5. Remove "Livingston" from the list using its name
stops.remove("Livingston")
print(stops)
print("this is the list with Livingston removed!")
print(" ")
#6. Delete "Cumbernauld" from the list by index
stops.remove(stops[2])
print(stops)
print("This is the list with Cumbernauld removed by it's index number!")
print(" ")
#7. Print the number of stops there are in the list
print(len(stops))
print("this is the number of stops in the list!")
print(" ")
#8. Sort the list alphabetically
sorted(stops)
print(sorted(stops))
print("This is the list organised alphabetically!")
print(" ")

#9. Reverse the positions of the stops in the list
reversed_list = stops[::-1]
print(reversed_list)
print("This is the list of stops reversed!")
print(" ")
#10 Print out all the stops using a for loop

for stop in stops:
    print(stop)
    
