# Matching multiple values with or (|)
# The | operator lets you group multiple patterns into a single case block
# The matched code runs when the value matches any one of the specified patterns
def holiday_check(day):
    match day:
        case "Saturday" | "Sunday":
            print(f"Hurray! {day} is a holiday")
        case _:
            print(f"Oops! {day}, it's a regular working day")


holiday_check("Saturday")
holiday_check("Monday")
