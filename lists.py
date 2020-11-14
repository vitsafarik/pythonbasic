# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create List
numbers = [1, 2, 3, 4, 5]
fruits = ["Apples", "Oranges", "Grapes", "Pears"]

# Use a construtor
# numbers2 = list((1, 2, 3, 4, 5))

print(numbers)

# Get a value
print(fruits[1])

# Get length
print(len(fruits))

# Change value
fruits[0] = "Blueberries"

# Apend to list
fruits.append("Mangos")

# Remove from list
fruits.remove("Grapes")

# Insert into position
fruits.insert(2, "Strawberries")

# Remove whit pop
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse Sort
fruits.sort(reverse=True)

print(fruits)