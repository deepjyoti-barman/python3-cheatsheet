# List comprehension
# Print numbers from 1 to 10
result = [i for i in range(1, 11)]
print(result)

# Print "hello" 5 times
result = ["hello" for _ in range(5)]
print(result)

# Print all words in uppercase
words = ["hello", "world", "python", "programming"]
result = [word.upper() for word in words]
print(result)

# Print only even numbers from 1 to 10
result = [i for i in range(1, 11) if i % 2 == 0]
print(result)

# Flatten a 2D matrix into a 1D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [element for row in matrix for element in row]
print(result)

# Flatten a 2D matrix into a 1D list and filter out odd numbers
result = [element for row in matrix for element in row if element % 2 == 0]
print(result)

# Create a dictionary from two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
result = {key: value for key, value in zip(keys, values)}
print(result)


# Ternary operator
# Basic example
number = 5
result = "Even" if number % 2 == 0 else "Odd"
print(result)

# Using with functions / lambda functions
even = lambda: "Even"
odd = lambda: "Odd"
result = even() if number % 2 == 0 else odd()
print(result)

# Using with list comprehension
result = [f"{i}=Even" if i % 2 == 0 else f"{i}=Odd" for i in range(1, 11)]
print(result)

# Using with dictionary comprehension
result = {i: "Even" if i % 2 == 0 else "Odd" for i in range(1, 11)}
print(result)
