# Version 2: House assignment using match-case
name = input("What's your name? ")  # Draco

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
