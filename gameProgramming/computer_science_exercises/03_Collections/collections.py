# Collections Examples, Eliot Blanton, v0.3a

#LIST -- Ordered Changeable, Allows duplicate values

breakfastFoods = ["Bacon", "Waffles", "Pancakes", "Cereal", "Milk"]

#Each item in the list is known as an element
#The postion in the list for each is known as the index
#The element bacon is at index 0
#index -1 is the last item in the list
testScores = [95, 100, 25, 15, 27, 35]
classGPA = [3.14, 2.25, 1.74, 1.99, 0.99, 4.25]

# printing contents of a list
#print (breakfastFoods)
#print (testScores)
#print (classGPA)

#Accessing specific list elements --  FIRST ELEMENT IS INDEX 0
#print(breakfastFoods[0])
#print(testScores[0])
#print(classGPA[0])

#Accessing last element in list

#print(breakfastFoods[-1])
#print(testScores[-1])
#print(classGPA[-1])

#Pause -- WYOC -- Access 3rd element in each list

#print(breakfastFoods[2])
#print(testScores[2])
#print(classGPA[2])

# changing items in a list
breakfastFoods[0] = "sausage"
testScores[0] = 97
classGPA[0] = 3.57

#print(breakfastFoods[0])
#print(testScores[0])
#print(classGPA[0])

#print(breakfastFoods)
#print(testScores)
#print(classGPA)

#pause WYOC -- change 5th element
#breakfastFoods[4] = "Eggs"
#testScores[4] = 3
#classGPA[4] = 0.75


#print(breakfastFoods)
#print(testScores)
#print(classGPA)

#Adding and inserting items to a list
#.append() adds an item to the end of a list
breakfastFoods.append("Hashbrowns")
print(breakfastFoods)
testScores.append(99)
print(testScores)
classGPA.append(1.99)
print(classGPA)

#.insert() Allows you to place an item at a specific index in the list
#breakfastFoods.insert(3, "Parfait")
#print(breakfastFoods)
#testScores.insert(3, 55)
#print(testScores)
#classGPA.insert(3, 0.0)
#print(classGPA)

#WYOC -- append an item to each list
#breakfastFoods.append("French toast")
#print(breakfastFoods)
#testScores.append(45)
#print(testScores)
#classGPA.append(2.87)
#print(classGPA)

#breakfastFoods.insert(4, "Toast")
#print(breakfastFoods)
#testScores.insert(4, 59)
#print(testScores)
#classGPA.insert(4, 3.23)
#print(classGPA)

#Deleting items from a list
#use .remove() to remove a specific item from the list
#breakfastFoods.remove("Waffles")
#print(breakfastFoods)
#testScores.remove(100)
#print(testScores)
#classGPA.remove(2.25)
#print(classGPA)

#To delete using the index value we use .pop
#breakfastFoods.pop(4)
#print(breakfastFoods)
#testScores.pop(4)
#print(testScores)
#classGPA.pop(4)
#print(classGPA)

#WYOC -- .pop() the second element from each list and .remove() any item from the list
#breakfastFoods.pop(1)
#testScores.pop(1)
#classGPA.pop(1)

#breakfastFoods.remove("Pancakes")
#testScores.remove(15)
#classGPA.remove(4.25)
#print(breakfastFoods)
#print(classGPA)
#print(testScores)

# Determining list length
print(f"There are {len(breakfastFoods)} items in the breakfast foods list")
print(f"There are {len(testScores)} items in the test scores list")
print(f"There are {len(classGPA)} items in the class GPA list")











