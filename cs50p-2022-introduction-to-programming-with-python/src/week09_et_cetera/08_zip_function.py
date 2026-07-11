# The zip function in Python is used to combine elements from multiple iterables
# (like lists, tuples, etc.) into tuples
# Basic usage
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 88]

paired = list(zip(names, scores))
print(paired)

# Iterating over multiple sequences
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# Unzipping
names, scores = zip(*paired)
print(names)
print(scores)


# Zip with different lengths
# When the input iterables have different lengths, the zip function will stop creating tuples
# when the shortest iterable is exhausted
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90]

paired = list(zip(names, scores))
print(paired)


# Zipping more than two lists
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 88]
ages = [25, 30, 35]

combined = list(zip(names, scores, ages))
print(combined)
