# Sort in the list
# Two ways: list method -- sort and built in function -- sorted
listOfElements = [10,20,30,45,1,5,23,223,44552,34,53,2]

# Difference between sort and sorted


print(sorted(listOfElements))   # Creates new sorted list
print(listOfElements)           # original list remains same

print(listOfElements.sort())  # Return None, make changes in the given list
print(listOfElements)

print(listOfElements.sort(reverse=True))  # Reverese sorting, Return None, make changes in the given list
print(listOfElements)