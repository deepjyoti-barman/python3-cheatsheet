# A variable is just a container for some value inside a computer
# Comments are notes to yourself and others in your code, comments can also serve to be a to-do list for yourself
name = input("What's your full name? ").strip().title()

# Syntax: print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
print("hello, " + name)

print("hello, ", end="")
print(name)

print("hello,", name)
print("hello, ", name, sep="")

# Format string (F-string)
print(f"hello, {name}")

# Split user's name into first name and last name
first, last = name.split(" ")

print(f"hello, {first}")
