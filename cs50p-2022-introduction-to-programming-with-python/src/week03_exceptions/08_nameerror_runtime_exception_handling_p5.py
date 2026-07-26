# Simplified modularized version without error message
# Also passing prompt as parameter to make it more flexible

def main():
    x = get_int('What is x? ')
    print(f'x is {x}')


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))  # input: cat | input: dog | input: bird | input: 20
        except ValueError:
            pass        # Silently ignore invalid input


main()