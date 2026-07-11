# Lambda function with no arguments and no return value
no_args = lambda: print("Hello, World!")

# Lambda function with one argument and no return value
one_arg = lambda x: print(f"Received value: {x}")

# Lambda function with two arguments and one return value
two_args = lambda x, y: x + y


# Call the lambda functions
no_args()
one_arg(5)
print(two_args(5, 10))
