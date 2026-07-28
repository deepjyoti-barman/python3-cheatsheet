try:
    total = 10 / 0
    print(total)
except ZeroDivisionError:
    print("Cannot divide by zero")