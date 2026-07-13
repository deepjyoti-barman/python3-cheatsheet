# CS50P - Lecture 1 - Conditionals

## Notes

- Conditionals, or conditional statements, in Python and in other languages are this ability to 
ask questions and answer those questions, in order to decide if you want to execute a line of code
or some other line of code instead.
- `if` statement is used to make decisions in the code.
- The condition inside the `if` statement must evaluate to a boolean value (True or False).
- If the condition is True, the code block under the `if` statement is executed.
- If the condition is False, the code block under the `if` statement is skipped.
- So, an `if` statement is a control flow statement used to execute a block of code only when a
specified condition is `True`.
- Syntax:

  ```python
  if condition:
      # Code to execute if condition is True
  ```

- An `if–else` statement is a control flow structure that allows the program to choose between two actions:
  - One block of code runs if the condition is `True`
  - The other block runs if the condition is `False`
- We can also use `elif` (else if) and `else` statements to handle multiple conditions.
- An `if–elif–else` statement is a control flow structure that allows you to check multiple conditions
and execute different blocks of code depending on which condition is `True`
- Nested `if` statements can be used to check multiple conditions.
- It's important to use proper indentation to ensure that the code blocks are correctly associated with their respective conditional statements.
- A `match` statement is a control flow structure used for pattern matching, allowing the program to
compare a value against different patterns and execute the block of code that matches.
- The `and` operator checks if both conditions are True.
- The `or` operator checks if at least one of the conditions is True.
- The `not` operator negates a boolean value.
