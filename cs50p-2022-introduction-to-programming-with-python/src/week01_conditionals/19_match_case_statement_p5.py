# match-case with dictionaries
# match-case can work with dictionaries by matching specific keys and their corresponding values
# It can also extract values from matching keys and store them in variables for further use
def person_info(data):
    match data:
        case {"name": name, "age": age}:
            print(f"Name: {name}, Age: {age}")
        case {"name": name}:
            print(f"Name: {name}")
        case _:
            print("Unknown format")


person_info({"name": "Emily", "age": 25})
person_info({"name": "Harry"})
person_info({"city": "New York"})
