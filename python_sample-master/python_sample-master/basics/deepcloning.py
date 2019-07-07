import copy

listOfElements = ["A", "B", 10, 20, [100, 200, 300]]


# newList= listOfElements.copy() -- list method- performs shallow copy

newList = copy.deepcopy(listOfElements)  # Deep copy -- method provided by copy module
newList1 = copy.copy(listOfElements)     # Shallow copy -- method provided by copy module

print("Before modification: \n\nOriginal List: ", listOfElements)

print("Copied List due to shallow cloning: ", newList1)

print("Copied List due to deep cloning: ", newList)

# Modification

listOfElements[1] = 100

newList[4][0] = 200

newList1[4][2] = 100

print("\n\nAfter modification: \n\nOriginal List: ", listOfElements)

print("Copied List due to shallow cloning: ", newList1)

print("Copied List due to deep cloning: ", newList)