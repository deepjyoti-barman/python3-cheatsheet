# Prompt user for a positive integer n and print "meow" n times
# This while is an important paradigm called input validation
# It ensures that the user enters a valid input
while True:
    n = int(input("What's n? "))  # 3

    if n > 0:
        break

for _ in range(n):
    print("meow")
