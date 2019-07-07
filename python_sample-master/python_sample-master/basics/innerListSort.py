# Inner List Sorting

def customFunction(innerList):
    return innerList[1]

listOfElements = [[30,"A"], [20, "B"], [10, "C"]]

print("Ascending Order: ")
listOfElements.sort(key=customFunction)
print(listOfElements)
print("Descending Order: ")
listOfElements.sort(key=customFunction, reverse=True)
print(listOfElements)

# Inner List Sorting

def customFunction1(innerList):
    return innerList[0]

print("Ascending Order: ")
listOfElements.sort(key=customFunction1)
print(listOfElements)

print("Descending Order: ")
listOfElements.sort(key=customFunction1, reverse=True)
print(listOfElements)
