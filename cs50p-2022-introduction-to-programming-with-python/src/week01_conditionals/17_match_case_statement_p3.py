# Adding conditions with guards
# Guards allow us to add extra checks to a pattern using the if keyword
# A case is executed only when the value matches the pattern and the specified condition evaluates to True
def num_check(num):
    match num:
        case n if n > 0:
            print("Positive number")
        case n if n < 0:
            print("Negative number")
        case _:
            print("Zero")


num_check(15)
num_check(-8)
num_check(0)
