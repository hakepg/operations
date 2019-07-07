listOfElements = ["A", "B", 10, 20, [100, 200, 300]]

newList = listOfElements.copy()

print(id(newList))
print(id(listOfElements))

print(newList == listOfElements)
print(newList is listOfElements)
print(id(newList) == id(listOfElements))

print("Original List: ", listOfElements)
print("Copied List: ", newList)

# Modification

listOfElements[1] = 100

newList[4][0] = 200

print("After modification: \nOriginal List: ", listOfElements)
print("Copied List: ", newList)

# Modification

listOfElements[1] = 100

newList[4] = 200

print("After modification: \nOriginal List: ", listOfElements)
print("Copied List: ", newList)