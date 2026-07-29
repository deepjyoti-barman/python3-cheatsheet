# Demonstration of finally block with 'FileNotFoundError' runtime exception

try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close()