# Print a square of size n x n using nested loops
def main():
    print_square(3)


def print_square(size):
    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):

            # Print a brick without moving to the next line
            print("# ", end="")

        print()  # Move to the next line after each row


main()
