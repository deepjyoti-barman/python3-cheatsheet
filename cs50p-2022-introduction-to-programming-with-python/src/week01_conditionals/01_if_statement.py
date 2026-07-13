# Version 1: Basic version with separate if statements
# Disadvantage: All conditions are checked even if one is already true
x = int(input("What's x? "))  # 1
y = int(input("What's y? "))  # 2

# x < y is a boolean expression, which evaluates to True or False
if x < y:
    print("x is less than y")

if x > y:
    print("x is greater than y")

if x == y:
    print("x is equal to y")
