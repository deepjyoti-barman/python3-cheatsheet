# Ask the user for their name, remove leading/trailing whitespace,tabs or newlines if any, and convert to title-case
# rstrip(): Removes unwanted characters from the right end only
# lstrip(): Removes unwanted characters from the left end only
# strip(): Removes unwanted characters from both ends of a string
# By default, they remove whitespace characters such as spaces, tabs (\t), and newlines (\n)
name = input("What's your full name? ").strip().title()
print("PS-1: hello, " + name)

# Syntax: print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
print("PS-2: hello, ", end="")
print(name)

print("PS-3: hello,", name)
print("PS-4: hello, ", name, sep="")

# Format string (F-string)
print(f"PS-5: hello, {name}")

# Splitting the name into first and last, then greeting with the first name
first, last = name.split(" ")
print(f"PS-6: hello, {first}")
