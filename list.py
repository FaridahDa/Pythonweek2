# example of list
fruits = ["Apple", "Mango", "Cherry"]
print(fruits)

#example of getting fruit from the list
print(fruits[1])

#example of getting the last fruit in the sequence
print(fruits[-1])

#length of the list
print(len(fruits))

#amending/adding to the list
fruits.append("Melon")
print(fruits)

#adding to the list
fruits2 = ["Strawberries", "Kiwis", "Grapes"]
fruits.extend(fruits2)
print(fruits)

#example of a set, why hasn't our set changed order & how do we create a loop with a set?
veg = {"sprouts", "onions", "lettuce", "carrots" }
print(veg)
print(veg)
print(veg)
x = 1
for x in veg:
    print(x)
