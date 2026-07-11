# Define the dictionary with lambda functions for each case
switch_dict = {
    1: lambda: "Monday",
    2: lambda: "Tuesday",
    3: lambda: "Wednesday",
    4: lambda: "Thursday",
    5: lambda: "Friday",
    6: lambda: "Saturday",
    7: lambda: "Sunday"
}

# Define the default lambda function
default = lambda: "Invalid day"

# Input value
input_value = 9

# Get the function from the dictionary based on the input value
# If the key is not found, return the default function
result = switch_dict.get(input_value, default)()

print(result)
