# match-case with sequences
# match-case can be used with sequences such as lists and tuples to check their structure and access individual elements
# It allows you to match sequences based on the number and arrangement of values they contain
def process(data):
    match data:
        case [x, y]:
            print(f"Two elements: {x}, {y}")
        case [x, y, z]:
            print(f"Three elements: {x}, {y}, {z}")
        case _:
            print("Unknown format")


process([1, 2])
process([1, 2, 3])
process([1, 2, 3, 4])
