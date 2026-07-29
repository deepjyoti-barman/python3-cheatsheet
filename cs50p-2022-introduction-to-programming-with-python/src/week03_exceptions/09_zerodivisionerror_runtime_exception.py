# Demonstration of 'ZeroDivisionError' runtime exception

def main():
    dividend, divisor = get_inputs()
    quotient = divide(dividend, divisor)
    if quotient is not None:
        print(f"dividend = {dividend}, divisor = {divisor}, result of division is {quotient}")


def get_inputs():
    while True:
        try:
            dividend = int(input("What's the value of dividend? "))
            divisor = int(input("What's the value of divisor? "))
            return dividend, divisor
        except ValueError:
            pass        # Silently ignore invalid input


def divide(dividend, divisor):
    try:
        return dividend / divisor
    except ZeroDivisionError:
        # Raising the exception with custom, explanatory message
        print(f"The divisor {divisor} is zero. Cannot divide the dividend by zero.")
        return None


main()