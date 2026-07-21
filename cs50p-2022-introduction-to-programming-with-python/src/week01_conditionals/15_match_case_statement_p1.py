"""
match-case statement

- match-case is Python's structural pattern matching statement
- It was introduced in Python 3.10 (PEP 634, released October 2021)
- Use case: cleanly compare a single value against multiple possible
patterns (literals, types, sequences, objects) and executes the code
block associated with the first match
- Difference from if-else: It provides a more organized, readable alternative
to long if-elif-else statements when handling multiple conditions, also supports
pattern matching (e.g. destructuring lists/tuples, matching object attributes),
which if-else cannot do directly
- The "case _:" acts as the default/fallback/wildcard case and runs when none of
the other patterns match, similar to "else"
"""


def check_number(num):
    match num:
        case 10:
            print("It's 10")
        case 20:
            print("It's 20")
        case _:
            print("It's neither 10 nor 20")


check_number(10)
check_number(30)
