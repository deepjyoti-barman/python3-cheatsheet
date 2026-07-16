# CS50P - Lecture 3 - Exceptions

## Notes

- Exceptions refer to problems in a program—errors that occur during execution and interrupt the
normal flow of instructions
- A syntax error is an error that occurs when the rules of the programming language are violated,
causing the program to fail before execution
- Syntax errors must be fixed by the developer. Such errors require the developer to review and 
correct the code directly, as they cannot resolve themselves or be handled by other parts of the program
- Runtime errors are errors that occur while a program is executing, after it has started running. 
These errors interrupt the normal flow of the program and usually happen due to invalid operations, 
such as dividing by zero, accessing an invalid index, or using an undefined variable
- One of the way to handle such runtime error is writing code defensively that anticipates and 
handles unexpected situations using exception handling (`try`, `except`, `else`, `finally`) to catch
and manage errors gracefully
- A `try–except` block allows you to test a block of code for errors (`try`) and execute alternative
code (`except`) if an exception occurs. It helps in gracefully handling errors, maintaining program
flow, and providing meaningful error handling instead of abrupt termination
- The `else` block is used with a `try–except` statement to define code that executes only if no
exception occurs in the `try` block. It helps separate error-prone code from code that should run 
only when no errors occur, making the program clearer and more readable
- The `finally` block is used with a `try–except` statement to define code that always executes,
whether an exception occurs or not. It is mainly used for cleanup actions, such as closing files,
releasing resources, or resetting variables
- The `raise` statement is used to explicitly trigger an exception when a specific condition occurs.
It helps enforce rules, validate conditions, and signal errors intentionally instead of allowing
the program to fail silently or behave incorrectly.
