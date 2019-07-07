# Data Types
#added from pycharm
# LIST

listOfElements=[10,20,30,40,50,"a"]
# Printing length of list using two ways
print(listOfElements.__len__())  # Specific method for list type of objects- inside class list
print(len(listOfElements))       # 64 build_in function

# Printing List elements
print("Printing List elements:")
print(listOfElements)

# Printing List elements using for
print("Printing List elements using for:")
for item in listOfElements:
    print(item)


# Printing List elements in reverse
print("Printing List elements in reverse:")
for item in listOfElements[::-1]:
    print(item)

# Printing List elements using slicing[start:stop:step]-- start is inclusive and stop is exclusive i.e. <
print("Printing List elements in reverse:")
for item in listOfElements[2:5:1]:
    print(item)

# Modifying element in the list

listOfElements[4]=500
print("After Modification using index and assignment:")
for item in listOfElements:
    print(item)

# Modifying element in the list- Using Insert

listOfElements.insert(10,100)
print("after insert:", listOfElements)

# Append in the list

listOfElements.append(400)  # Equivalent of insert-- listOfElements.insert(len,obj)
print("after append: ", listOfElements)

# Remove method in the list

print("Removed Element mentioned- 100: ", listOfElements.remove(100))
print(listOfElements)

# Difference between append and extend

listOfElements.append([10,20,30])
print("After Append: ", listOfElements)
print(len(listOfElements))

listOfElements.extend([10,20,30])
print("After Extend: ", listOfElements)
print(len(listOfElements))

# Printing elements from 0-4

print("Printing elements from 0-4: ")
for item in range(5):
    print(item)

# Remove all 20's present in the list
count=0

for item in listOfElements:
    if type(item)==list:
        count+=item.count(20)
count+=listOfElements.count(20)

print(count)

for sr in range(listOfElements.count(20)):
    listOfElements.remove(20)

print("After removing 20's in the list: ", listOfElements)

# Difference between clear and remove

listOfElements.remove(10)
print("After Remove: ", listOfElements)

listOfElements.clear()
print("After Clear: ", listOfElements)
