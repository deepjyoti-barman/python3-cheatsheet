# Arithmetic operations with integers
x = int(input("What's the value of x? "))  # 3
y = int(input("What's the value of y? "))  # 1
print("PS-1:", x + y)  # 4

# ---------------------------------------------------------------------------------------

# Arithmetic operations with floating point numbers
p = float(input("What's the value of p? "))  # 999.5
q = float(input("What's the value of q? "))  # 0.5

# Rounding off the result and separate numeric output greater than 1000 with commas
# Syntax: round(number[, ndigits])
r = round(p + q)
print(f"PS-2: {r:,}")  # 1,000

# ---------------------------------------------------------------------------------------
d = float(input("What's the value of d? "))  # 2
e = float(input("What's the value of e? "))  # 3

# Round off to 2 decimal places
f = round(d / e, 2)
print("PS-3:", f)  # 0.67

# Round off to 2 decimal places with F-string
print(f"PS-4: {f:.2f}")  # 0.67
