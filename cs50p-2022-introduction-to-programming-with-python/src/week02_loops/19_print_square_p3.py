# Final refactored version of printing a square without a helper function
def main():
    print_square(3)


def print_square(size):
    for _ in range(size):
        print("# " * size)


main()
