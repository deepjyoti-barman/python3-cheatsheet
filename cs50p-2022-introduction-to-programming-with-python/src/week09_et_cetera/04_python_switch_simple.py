def day_1():
    return "Monday"


def day_2():
    return "Tuesday"


def day_3():
    return "Wednesday"


def day_4():
    return "Thursday"


def day_5():
    return "Friday"


def day_6():
    return "Saturday"


def day_7():
    return "Sunday"


def default():
    return "Invalid day"


# Dictionary mapping keys to functions
switch_dict = {
    1: day_1,
    2: day_2,
    3: day_3,
    4: day_4,
    5: day_5,
    6: day_6,
    7: day_7
}

# Input value
input_value = 4

# Get the function from the dictionary based on the input value
# If the key is not found, return the default function
result = switch_dict.get(input_value, default)()

print(result)
