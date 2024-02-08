# Python 3 Cheatsheet

## Python Installations

### GUI installers

- Download from the link: [https://www.python.org/downloads/](https://www.python.org/downloads/)

### CLI installers

#### Using brew

- python@3.11 `brew install python@3.11`
- python-tk@3.11 (required to access `idle3` command from Terminal) (install via
  `brew install python-tk@3.11`)

#### Using pyenv - Simple Python Version Management tool

- pyenv lets you easily switch between multiple versions of Python. It's simple, unobtrusive, and
  follows the UNIX tradition of single-purpose tools that do one thing well.
- Official documentation: [https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv)
- Introduction to pyenv:
  [https://realpython.com/intro-to-pyenv/](https://realpython.com/intro-to-pyenv/)

##### Commonly used pyenv commands

- `pyenv install --list`: This command lists all available python versions, you can use grep to find
  a specific Python version
- `pyenv install --list | grep " 3\.[678]"`: List all the available CPython 3.6 through 3.8
- `pyenv install 2.7.15`: This command can be used to install a specific version of Python.
- `pyenv install -v 3.11.5`: The install command with -v flag ensures to display all the steps of
  installing the specified version of Python.
- `pyenv uninstall 2.7.15`: This command can be used to uninstall a specific version of Python.
- `pyenv versions`: The versions command displays all currently installed Python versions
- `pyenv version`: This command is similar to versions but only shows you the current active Python
  version.
- `pyenv which python`: The which command is helpful for determining the full path to a system
  executable. Because pyenv works by using shims, this command allows you to see the full path to
  the executable pyenv is running. The output displays the full system path for pip. This can be
  helpful when you’ve installed command-line applications.

##### Installation and configuration to support multiple Python versions

```bash
# Install pyenv via brew
brew install pyenv

# Install the latest versions of python2 and python3
pyenv install 2.7.18
pyenv install 3.12.0

# Set both python2 and python3 globally accessible
pyenv global 2.7.18 3.12.0

# Append the following line at the end of '.zshrc'/'.bashrc' file depending on your default shell
# Note: Appending the following line may not work in '.zshenv' / '.bashenv' / '.bash_profile' etc. files
export PATH=$(pyenv root)/shims:$PATH

# Verification of configuration
# python/python2 -> Should point to Python 2.7.18
# python3 -> Should point to Python 3.12.0
which python
# /Users/deepjyoti.barman/.pyenv/shims/python

which python3
# /Users/deepjyoti.barman/.pyenv/shims/python3

pyenv which python
# /Users/deepjyoti.barman/.pyenv/versions/2.7.18/bin/python

pyenv which python3
# /Users/deepjyoti.barman/.pyenv/versions/3.12.0/bin/python3
```

## Editors for Python

- Visual Studio Code
- PyCharm Community Edition

## Visual Studio Code Configurations

### Visual Studio Code Extensions

- Better Comments
- Black Formatter
- Code Runner
- CodeSnap
- DotENV
- EditorConfig for VSCode
- Git Blame
- Git Graph
- Git History
- Image Preview
- Material Icon Theme
- One Dark Darker
- Path Intellisense
- Playwright Test for VSCode
- Prettier - Code formatter
- Project Manager
- Python
- Tabnine: AI Autocomplete...
- TODO Highlight
- Todo Tree

### Visual Studio Code Settings

```json
{
  // "c-cpp-compile-run.c-flags": "-Wall -Wextra -O0 -std=c18",
  // "c-cpp-compile-run.cpp-flags": "-Wall -Wextra -O0 -std=c++20",

  "code-runner.clearPreviousOutput": true,
  "code-runner.executorMap": {
    "python": "python3 -u",
    "typescript": "tsc"
  },
  "code-runner.ignoreSelection": true,
  "code-runner.runInTerminal": true,
  "code-runner.saveFileBeforeRun": true,
  "code-runner.showExecutionMessage": true,

  "color-highlight.markerType": "dot-after",

  "cSpell.ignoreWords": ["deepjyoti"],

  "diffEditor.ignoreTrimWhitespace": false,

  "editor.fontSize": 11,
  "editor.suggestSelection": "first",
  "editor.wordWrap": "on",
  "editor.minimap.scale": 2,
  "editor.minimap.autohide": true,
  "editor.minimap.renderCharacters": false,
  "editor.fontFamily": "Cascadia Mono, Monolisa, Menlo, Monaco, 'Courier New', monospace, Consolas",
  "editor.formatOnSave": true,
  "editor.formatOnPaste": true,
  "editor.bracketPairColorization.enabled": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",

  "explorer.compactFolders": false,
  "explorer.confirmDelete": false,
  "explorer.confirmDragAndDrop": false,

  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 4000,

  "prettier.singleQuote": false,
  "prettier.tabWidth": 4,

  "playwright.reuseBrowser": false,

  "security.workspace.trust.untrustedFiles": "open",

  "terminal.integrated.fontFamily": "Monaco",
  "terminal.integrated.fontSize": 10,

  "tabnine.experimentalAutoImports": true,

  "workbench.colorTheme": "One Dark Darker",
  "workbench.iconTheme": "material-icon-theme",

  // Configuration for extension "Language Support for Java(TM) by Red Hat"
  "redhat.telemetry.enabled": true,
  "[java]": {
    "editor.defaultFormatter": "redhat.java"
  },

  // Configuration for extension "Black Formatter"
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter"
  },
  "black-formatter.args": ["--line-length", "100", "--skip-string-normalization"]
}
```

### Create Virtual Environments in VSCode

#### Command-line approach

- Open up the directory where you want the virtual environment to be created in Terminal
- Type the command: `python3 -m venv <venv-directory-name>`
- Above command will create a virtual environment with the default Python version installed on your
  system.
- Alternatively if you want to create a virtual environment with a different Python version, you can
  use this command: `</path/to/python> -m venv <venv-directory-name>`
- Activation and deactivation commands:

  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  deactivate
  ```

#### Create virtual environment using VSCode extension

- Install a VSCode extension called 'Python' from marketplace
- Open up the directory where you want the virtual environment to be created in VSCode
- Press `Command + Shift + P` to open up command palette
- Search and select the option 'Python: Create Environment...'
- Select environment type as 'venv'
- Choose Python interpreter version
- Virtual environment with the given Python interpreter version will be inside on the '.venv'
  directory

## PyCharm Community Edition Configurations

### PyCharm CE Extensions

## Python

### Basics

```python
# Printing 'Hello, World!'
print('Hello, World!')

# Printing in different lines using one print() statement
print('Deepjyoti Barman\n I am learning Python')

# Printing multiple lines of strings exactly as it is
st = '''
    Hello I am Deepjyoti Barman,
    I work in MakeMyTrip India Pvt. Ltd.
    and currently I am learning Python
    '''
print(st)

# Python indentation rules
x = 4 + 4
x = 4 \
    + 4

# This is a single line comment
'''
    This is a
    multi-line
    comment
'''
```

### User Inputs

```python
x = input('Enter a number: ')
print(x)
```

### Variables

```python
# Added shebang as the following is a way of providing the default path where the python interpreter is installed, useful for mac/linux platforms
#!/usr/bin/python3
bank_account = 12223445

# Basic assignment
score = 23323
high_score = 334545
winner_name = 'Deepjyoti Barman'
winner_score = 7839

# Reserved keywords given below should not be used as a variable name
# and    exec    not
# as    finally    or
# assert    for    pass
# break    from    print
# class    global    raise
# continue    if    return
# def    import    try
# del    import    while
# elif    is    with
# else    lambda    yield
# except

# Chain assignment
x = y = z = 1
print(y)

# Comma separated variable assignment
x, y, z = 4, 5, 'Deep'
print(z)

# Standard type of variables:
# Numbers
# String
# List
# Tuple
# Dictionary
```

### Numbers

```python
# Numbers: int, float, complex
bank_uid = 123456
bank_balance = 455.9
imaginary_no = 4 + 5j

print(type(bank_uid))
print(type(bank_balance))
print(type(imaginary_no))

# Delete the reference from the memory
del bank_balance
```

### Strings

```python
# Strings
st = 'Hello World!'
print(st)               # Hello World!
print(st[1])            # e
print(st[3:5])          # lo
print(st[3:])           # lo World!
print(st[:5])           # Hello
print(str + ' Dj')      # Hello World! Dj
print(4 + '4')          # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print('4' + 4)          # TypeError: can only concatenate str (not "int") to str

# ----------------------------------------------------------------
# String methods
myStr = 'This is a string'

# Return a capitalized version of the string
print(myStr.capitalize())                   # This is a string

# Return a version of the string where each word is titlecased
print(myStr.title())                        # This Is A String

# Convert uppercase characters to lowercase and lowercase characters to uppercase.
print(myStr.swapcase())                     # tHIS IS A STRING

# Return a copy of the string converted to uppercase
print(myStr.upper())                        # THIS IS A STRING

# Return a copy of the string converted to lowercase
print(myStr.lower())                        # this is a string

# Return a version of the string suitable for case-less comparisons
print(myStr.casefold())                     # this is a string

# Return a centered string of length width.
print(myStr.center(24, '-'))                # ----This is a string----

# Return the number of non-overlapping occurrences of substring
print(myStr.count('i'))                     # 3
print(myStr.count('i', 3))                  # 2
print(myStr.count('i', 3, 7))               # 1

# Return True if the string ends with the specified suffix
print(myStr.endswith('string'))             # True
print(myStr.endswith('a string', 8))        # True
print(myStr.endswith('a string', 5, 7))     # False

# Return True if the string starts with the specified prefix
print(myStr.startswith('This'))             # True
print(myStr.startswith('is', 5))            # True
print(myStr.startswith('is', 5, 6))         # False

# Return a copy of the string with leading and trailing whitespace removed
name = '    Deepjyoti----'
print(name.strip('-').strip())              # Deepjyoti
print(name.rstrip('-'))                     #     Deepjyoti
print(name.lstrip())                        # Deepjyoti----

# Return a copy where all tab characters are expanded using spaces
txt = "H\te\tl\tl\to"
print(txt.expandtabs(2))                    # H e l l o

# Return the lowest index in S where substring sub is found
print(myStr.find('is'))                     # 2
print(myStr.find('111'))                    # -1
print(myStr.find('is', 1))                  # 2
print(myStr.find('is', 5, 10))              # 5

# Return the highest index in S where substring sub is found
print(myStr.rfind('is'))                    # 5

# Return the lowest index in S where substring sub is found
# Raises ValueError when the substring is not found
print(myStr.index('is'))                     # 2
# print(myStr.index('111'))                  # ValueError
print(myStr.index('is', 1))                  # 2
print(myStr.index('is', 5, 10))              # 5

# Return the highest index in S where substring sub is found
print(myStr.rindex('is'))                    # 5

# Use of format() and format_map() methods
name_map = {'f_name':'John', 'l_name':'Wick'}
print('{f_name}\'s last name is {l_name}'.format(**name_map))           # John's last name is Wick
print('{f_name}\'s last name is {l_name}'.format_map(name_map))         # John's last name is Wick

print('B12'.isalnum())                      # True
print('A'.isalpha())                        # True
print('ABDC'.isascii())                     # True
print('9280.50'.isdecimal())                # False
print('123'.isdigit())                      # True
print('1_name'.isidentifier())              # False
print('apple'.islower())                    # True
print('INDIA'.isupper())                    # True
print('123'.isnumeric())                    # True
print(myStr.isprintable())                  # True
print('    '.isspace())                     # True
print('I Love My India'.istitle())          # True

# Return a left-justified string of length width
# Padding is done using the specified fill character (default is a space)
print(myStr.ljust(24, '-'))                 # This is a string--------
print(myStr.rjust(24, '-'))                 # --------This is a string

# Return a copy with all occurrences of substring old replaced by new
# replace(old: str, new: str, count: int=..., /) -> str
# count = Maximum number of occurrences to replace
# -1 (the default value) means replace all occurrences
print(myStr.replace('is', 'iss', 1))        # Thiss is a string

# Return a list of the substrings in the string, using sep as the separator string
# split(sep: Optional[str]=..., maxsplit: int=...) -> List[str]
# maxsplit = Maximum number of splits (starting from the left)
# -1 (the default value) means no limit
print(myStr.split())                        # ['This', 'is', 'a', 'string']
print(myStr.split(sep=' ', maxsplit=-1))    # ['This', 'is', 'a', 'string']
print(myStr.split(maxsplit=1))              # ['This', 'is a string']

# Return a str with the given prefix string removed if present
print(myStr.removeprefix('This'))           #  is a string

# Return a str with the given suffix string removed if present
print(myStr.removesuffix('string'))         # This is a

# Partition the string into three parts using the given separator
# If the separator is not found, returns a 3-tuple containing the original string and two empty strings
# Search for the word "bananas", and return a tuple with three elements:
# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"
sentence = 'I could eat bananas all day'
print(sentence.partition("bananas"))        # ('I could eat ', 'bananas', ' all day')
print(sentence.partition("apple"))          # ('I could eat bananas all day', '', '')

# This will search for the separator in the string, starting at the end
# If the separator is not found, returns a 3-tuple containing two empty strings and the original string
print(sentence.rpartition("bananas"))       # ('I could eat ', 'bananas', ' all day')
print(sentence.rpartition("apple"))         # ('', '', 'I could eat bananas all day')

# splitlines() method splits a string into a list
# The splitting is done at line breaks
# Optional parameter = keeplinebreaks, specifies if the line breaks should be included (True), or not (False)
# Default value is False
note = "Thank you for the music\nWelcome to the jungle"
print(note.splitlines())                    # ['Thank you for the music', 'Welcome to the jungle']
print(note.splitlines(True))                # ['Thank you for the music\n', 'Welcome to the jungle']

# zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length
# If the value of the len parameter is less than the length of the string, no filling is done
a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))                          # 00000hello
print(b.zfill(10))                          # welcome to the jungle
print(c.zfill(10))                          # 000010.000

# ----------------------------------------------------------------
# String concatenation
name = 'Deepjyoti'

# String concatenation using '+' operator
print('Hello ' + name)

# NOTE: Concatenation of a string with a numeric type is not possible
# str() method can be used to convert the numeric type into string type and then concatenate using '+' operator
print('My favorite number: ' + str(4))


# String concatenation using ',' operator
# Default delimiter as ' ' (one empty space)
# ',' operator can be used to concatenate any type of operand
print('I', 'love', 'my', 'India')


# String concatenation using join() method
# NOTE: Concatenation of a string with a numeric type is not possible
# Syntax: '<delimiter>'.join([str1, str2, str3, ..., strN])
print('-'.join(['Hello India has won the game by', str(32), 'runs']))


# String concatenation using '%' operator
# Format specifiers: %d = integer, %f = float, %s = string literal
# .2f = prints the value up to 2 decimal places (first 2 digits after the decimal point)
print('%s has won %d gold medals with an avg rating of %.2f in every game' % ('Keerthi', 4, 85.9))


# String concatenation using format() method
# Usage-1
print('{}, {} and {} will remain best friends forever'.format('Keerthi', 'Deepjyoti', 'Padmini'))

# Usage-2
print('{2}, {1} and {0} will remain best friends forever'.format('Keerthi', 'Deepjyoti', 'Padmini'))

# Usage-3
print('{arg2}, {arg1} and {arg3} will remain best friends forever'.format(arg1='Keerthi', arg2='Deepjyoti', arg3='Padmini'))


# String concatenation using f-string
# From, Python 3.6+ we can use f-string for string concatenation
name = 'Padmini'
chocolate_amt = 4
roses_amt = 7
proposals_amt = 3

print(f'{name} got {chocolate_amt} chocolates, {roses_amt} roses and {proposals_amt} proposals on Valentine\'s Day')

# ----------------------------------------------------------------
# Additional operations on String
str = 'Hello World'

# Check if the substring is present in the given string
if 'llo' in str:
    print('Match found: %s' % str)                              # Match found: Hello World

# Check if the string contains None or empty
print(str if str else 'String is empty or contains None')       # Hello World

str = ''
print(str if str else 'String is empty or contains None')       # String is empty or contains None

str = None
print(str if str else 'String is empty or contains None')       # String is empty or contains None
```

### List

```python
myListOne = [4, 5.8, 'Deepjyoti']
myListTwo = [55, 66, 'Barman']
print(type(myListOne))          # <class 'list'>
print(myListOne)                # [4, 5.8, 'Deepjyoti']
print(myListOne[2])             # Deepjyoti
print(myListOne[1:3])           # [5.8, 'Deepjyoti']
print(myListOne[-1])            # Deepjyoti
print(len(myListOne))           # 3
print(myListOne * 2)            # [4, 5.8, 'Deepjyoti', 4, 5.8, 'Deepjyoti']
print(myListOne + myListTwo)    # [4, 5.8, 'Deepjyoti', 55, 66, 'Barman']

# List element manipulation
myListOne[0] = 7
print(myListOne)                # [7, 5.8, 'Deepjyoti']

# Deep copy - both the references pointing to the same object
myListThree = myListOne
myListThree[0] = 8
print(myListOne)                # [8, 5.8, 'Deepjyoti']
print(myListThree)              # [8, 5.8, 'Deepjyoti']

# Shallow copy
myListFour = myListOne.copy()
myListFour[0] = 100
print(myListFour)               # [100, 5.8, 'Deepjyoti']
print(myListOne)                # [8, 5.8, 'Deepjyoti']

# Append object to the end of the list
myListTwo.append(22)
print(myListTwo)                # [55, 66, 'Barman', 22]

# Return number of occurrences of value
print(myListTwo.count(55))      # 1
print(myListTwo.count(99))      # 0

# Extend list by appending elements from the iterable
myListTwo.extend([44, 99, 55])
print(myListTwo)                # [55, 66, 'Barman', 22, 44, 99, 55]

# Return first index of value
# Raises ValueError if the value is not present
print(myListTwo.index('Barman'))                # 2
print(myListTwo.index(55, 2))                   # 6
print(myListTwo.index(55, 2, len(myListTwo)))   # 6

# Insert object before index
myListTwo.insert(0, 'Deepjyoti')
print(myListTwo)                # ['Deepjyoti', 55, 66, 'Barman', 22, 44, 99, 55]

# Remove and return item at index (default last)
# Raises IndexError if list is empty or index is out of range
print(myListTwo.pop())          # 55
print(myListTwo)                # ['Deepjyoti', 55, 66, 'Barman', 22, 44, 99]
print(myListTwo.pop(3))         # Barman
print(myListTwo)                # ['Deepjyoti', 55, 66, 22, 44, 99]

# Remove first occurrence of value
# Raises ValueError if the value is not present
myListTwo.remove('Deepjyoti')
print(myListTwo)                # [55, 66, 22, 44, 99]

# Syntax: def sort(*, key: None=..., reverse: bool=...) -> None
# Sort the list in ascending order and return None.
# If a key function is given, apply it once to each list item and sort them, ascending or descending, according to their function values.
# The reverse flag can be set to sort in descending order.
myListTwo.sort()
print(myListTwo)                # [22, 44, 55, 66, 99]

# Reverses all the items present in the list
myListTwo.reverse()
print(myListTwo)                # [99, 66, 55, 44, 22]

# Remove all items from list
myListTwo.clear()               # []
print(myListTwo)

# Removing an item from list
shopping_list = ['iPhone', 'Washing Machine', 'Fridge', 'Headphones']
del shopping_list[1]
print(shopping_list)            # ['iPhone', 'Fridge', 'Headphones']

# Sum of all the elements in a list
lst = [1, 2, 3, 4, 5]
print(sum(lst))                 # 15
```

### Tuple

```python
# Tuple - immutable in nature, objects contained in the tuple cannot be altered
# Tuple is also known as read only lists
myTupleOne = (4, 'Deepjyoti', 5.6, 'Barman')
myTupleTwo = (5, 2, 'Ram', 2)
print(type(myTupleOne))         # <class 'tuple'>
print(myTupleOne)               # (4, 'Deepjyoti', 5.6, 'Barman')
print(myTupleOne[1])            # Deepjyoti
print(myTupleOne[1:3])          # ('Deepjyoti', 5.6)
print(len(myTupleTwo))          # 3
print(myTupleOne * 2)           # (4, 'Deepjyoti', 5.6, 'Barman', 4, 'Deepjyoti', 5.6, 'Barman')
print(myTupleOne + myTupleTwo)  # (4, 'Deepjyoti', 5.6, 'Barman', 5, 2, 'Ram', 2)

myTupleOne[1] = 'Trello'        # TypeError: 'tuple' object does not support item assignment

# Return number of occurrences of value
print(myTupleOne.count(4))      # 1
print(myTupleOne.count(99))     # 0

# Return first index of value
# Raises ValueError if the value is not present
print(myTupleTwo.index(2))                        # 1
print(myTupleTwo.index(2, 2))                     # 3
print(myTupleTwo.index(2, 2, len(myTupleTwo)))    # 3

# Hack to insert elements into a tuple
basket1 = ('Apple', 'Banana', 'Mango')
basket2 = ('Mango', 'Jackfruit', 'Watermelon')
large_basket = basket1 + basket2
print(large_basket)             #  ('Apple', 'Banana', 'Mango', 'Mango', 'Jackfruit', 'Watermelon')

# Sum of all the elements in a tuple
tup = (1, 2, 3, 4, 5)
print(sum(tup))
```

### Set

```python
# Set does not maintain the order of elements
# Set does not contain any duplicates
chessboard_set = {'pawn', 'bishop', 'knight', 'rook', 'queen', 'king', 'bishop'}

# Printing the set
print(chessboard_set)                           # {'bishop', 'queen', 'king', 'rook', 'pawn', 'knight'}

# Length of the set
print(len(chessboard_set))                      # 6

# Verify if the set contains the given item
if 'rook' in chessboard_set:
    print('rook is present')                    # rook is present

# Verify if the set does not contain the given item
if 'jack' not in chessboard_set:
    print('jack is not present')                # jack is not present

# Adding an element to the set
cards_set = {'king', 'queen', 'jack'}
cards_set.add('ace')
print(cards_set)                                # {'ace', 'queen', 'jack', 'king'}

# Shallow copy of the set
new_cards_set = cards_set.copy()

# Remove an item from the set
new_cards_set.pop()
print(cards_set)                                # {'ace', 'queen', 'jack', 'king'}
print(new_cards_set)                            # {'queen', 'jack', 'king'}

# Get the difference of two sets
print(cards_set.difference(new_cards_set))      # {'ace'}

# Remove all elements of second set from first set
cloned_cards_set_1 = cards_set.copy()
cloned_cards_set_1.difference_update(new_cards_set)
print(cloned_cards_set_1)                       # {'ace'}

# Get the intersection of two sets
print(cards_set.intersection(new_cards_set))    # {'queen', 'jack', 'king'}

# Update the first set with the intersection of itself and the second set
cloned_cards_set_2 = cards_set.copy()
cloned_cards_set_2.intersection_update(new_cards_set)
print(cloned_cards_set_2)                       # {'queen', 'jack', 'king'}

# Verify if two sets are disjoint sets
# A pair of sets which does not have any common element are called disjoint set
set_a = {1, 2, 3}
set_b = {4, 5}
set_c = {1, 2, 3, 4, 5}
print(set_a.isdisjoint(set_b))                  # True

# Verify if the first set is a subset of the second set
print(set_a.issubset(set_c))                    # True

# Verify if the first set is a superset of the second set
print(set_c.issuperset(set_a))                  # True

# Remove an element from a set; it must be a member
# If the element is not a member, raise a KeyError
set_c.remove(5)
print(set_c)                                    # {1, 2, 3, 4}

# Symmetric difference: (A union B) - (A intersection B)
# Get the symmetric difference between two sets
print(set_c.symmetric_difference(set_b))        # {1, 2, 3, 5}

# Update the first set with the symmetric difference of itself and the second set
set_c.symmetric_difference_update(set_b)        # {1, 2, 3, 5}
print(set_c)

# Get the union of two sets
print(set_a.union(set_b))                       # {1, 2, 3, 4, 5}

# Update the first set with the union of itself and second set
set_a.update(set_b)
print(set_a)                                    # {1, 2, 3, 4, 5}

# Remove all the items from the set
set_a.clear()
print(set_a)                                    # set()
```

### Dictionary

```python
# Dictionary - helps in providing name for each index of a list
# Also known as lists having named indexes
# LHS i.e. the key/index can be a string, or a number
# RHS i.e. value can be any python object
myDictOne = {
  'One': 1,
  2: 2,
  'List One': [1, 2, 3, 4]
}
print(type(myDictOne))          # <class 'dict'>
print(myDictOne)                # {'One': 1, 2: 2, 'List One': [1, 2, 3, 4]}
print(myDictOne['One'])         # 1
print(myDictOne.keys())         # dict_keys(['One', 2, 'List One'])
print(myDictOne.values())       # dict_values([1, 2, [1, 2, 3, 4]])
print(myDictOne.items())        # dict_items([('One', 1), (2, 2), ('List One', [1, 2, 3, 4])])
print(len(myDictOne))           # 3
print(myDictOne.get('One'))     # 1

# Update the value of the key if the key is present, else inserts the key value pair into the dictionary
myDictOne.update({'One': 3})
print(myDictOne)                # {'One': 3, 2: 2, 'List One': [1, 2, 3, 4]})

# Remove and return a (key, value) pair as a 2-tuple
# Raises KeyError if the dictionary is empty
print(myDictOne.popitem())      # ('List One', [1, 2, 3, 4])
print(myDictOne)                # {'One': 3, 2: 2}

# Given the key returns the value, and removes the key value pair
# Raises KeyError if key not found
print(myDictOne.pop('One'))     # 3
print(myDictOne)                # {2: 2}

# Shallow copy
myDictTwo = myDictOne.copy()
myDictTwo.update({2: 'Two'})
print(myDictOne)                # {2: 2}
print(myDictTwo)                # {2: 'Two'}

# setdefault() method returns the value of the item with the specified key. If the key does not exist, insert the key, with the specified value
print(myDictOne.setdefault('Four', '4'))  # 4
print(myDictOne)                # {2: 2, 'Four': '4'}

# fromkeys() method returns a dictionary with the specified keys and the specified value.
keys = range(4)
default = ['One', 'Two']
myNewDict = dict.fromkeys(keys)
print(myNewDict)                # {0: None, 1: None, 2: None, 3: None}
myNewDict = dict.fromkeys(keys, default)
print(myNewDict)                # {0: ['One', 'Two'], 1: ['One', 'Two'], 2: ['One', 'Two'], 3: ['One', 'Two']}

# Remove all items from dictionary
myDictOne.clear()
print(myDictOne)                # {}
```

### Operators

```python
valOne = 32
valTwo = 5

# Arithmetic operators
print(valOne + valTwo)      # 37
print(valOne - valTwo)      # 27
print(valOne * valTwo)      # 160
print(valOne / valTwo)      # 6.4
print(valOne // valTwo)     # 6
print(valOne % valTwo)      # 2
print(valOne ** 2)          # 1024

# Comparison operators
print(valOne == valTwo)     # False
print(valOne != valTwo)     # True
print(valOne < valTwo)      # False
print(valOne > valTwo)      # True
print(valOne <= valTwo)     # False
print(valOne >= valTwo)     # True

# Logical operators
x = False
y = True
print(x and y)              # False
print(x or y)               # True
print(not x)                # True

# Membership operators
myList = [2, 35, 6, 7, 86, 44]
myVal = 1
print(myVal in myList)      # False
print(myVal not in myList)  # True

# Identity operators
# Mostly used in databases
a = 100
c = 100
print(id(a))                # 4515618400
print(id(c))                # 4515618400
print(a is c)               # True
p = [1, 2, 3]
q = [1, 2, 3]
print(id(p))                # 4483092416
print(id(q))                # 4483396672
print(p is q)               # False

# Bitwise operators
d = 6
e = 3
f = 2
print(d & e)                # 2
print(d | e)                # 7
print(d ^ e)                # 5
print(~e)                   # -4 (3 = 00000011 = 11111100 = -4)
print(d >> f)               # 1 (6 = 0110 = 0011 = 0001 = 1)
print(d << f)               # 24 (6 = 00110 = 01100 = 11000 = 24)
```

### Conditionals

```python
# if statement
age = 19

if (age >= 18):
    print('Welcome! you are allowed to the party')

# if-else statement
score = int(input('What is your score? '))

if score < 30:
    print('Hey! please try again')
else:
    print('Great score!')

# if-elif-else statement
user_rating = int(input('Enter the rating between 1-5: '))

if 1 <= user_rating <= 2:
    print('Sorry to hear about your experience')
elif 3 <= user_rating <= 4:
    print('We almost missed the perfect rating from you')
elif user_rating == 5:
    print('Happy to know that you loved our services')
else:
    print('Please enter rating between 1-5 only')

# match-case statement
alphabet = input('Enter any english alphabetic character: ').lower()

match alphabet:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print('You have entered a vowel')
    case _:
        print('That\'s a consonant')
```

### Loops

```python
# while-loop - used to run a block code until a certain condition is met
# while loop may have an optional else block
# The else part is executed after the condition of the loop evaluates to False
# The else block will not execute if the while loop is terminated by a break statement
score = 0

while score <= 10:
    print('Your score is:', score)
    score += 1
else:
    print('Your loop is exhausted')

# for loop - used to iterate over sequences such as lists, tuples, string, etc.
# for loop can have an optional else block
# The else part is executed when the loop is exhausted (after the loop iterates through every item of a sequence)
# The else block will not execute if the for loop is stopped by a break statement
languages = ['Swift', 'Python', 'Go', 'JavaScript']

for language in languages:
    if language == 'Go':
        break
    print(language)
else:
    print('All the languages are printed in the console')

# break-statement
# example 1
fruits = ['mango', 'apple', 'orange', 'jackfruit', 'banana', 'strawberry']
print('First 3 fruits are: ')
count = 0

for fruit in fruits:
    print(fruit)
    count += 1

    if count == 3:
        break

# example 2
user_input = int(input('Enter a value: '))

for list_number in list(range(1, 100)):
    if list_number == user_input:
        print('We got a match')
        break
else:
    print('No match found')
print('The loop has been terminated')

# continue-statement
for i in range(1, 11):
    if i % 2 == 1:
        continue

    print(f'{i} is even')

# pass statement
# The pass statement is a null statement which can be used as a placeholder for future code
# The indentation block of the for loop in python cannot be left blank
# Leaving the body of the for loop blank would result in an error
# If for some reason, we are required to leave the for loop body blank, then we use a pass statement
# Python program having an empty loop
name = 'Interviewbit'
for alphabet in name:
    pass
print(f'Last letter is {alphabet}')         # Last letter is t
```

### Functions

```python
# Function with no param and no return value
def display():
    '''function docstring'''
    print('I want to learn python')
    return

display()


# Function with one param and no return value
def greetings(name):
    print('Hello,', name)

greetings('David')


# Function with optional arguments
def user_creation(name, email, phone=None):
    print('Name =', name)
    print('Email =', email)
    print('Phone =', phone)

user_creation('Arvind', 'arvind.rathod@gmail.com')


# Function with two param and one return value
def cal_sum(num1, num2):
    return num1 + num2

print(cal_sum(47, 53))


# Function with variable no of arguments
def add_num(*num):
    return sum(num)

print(add_num(1, 2, 3, 4, 5))


# Function with keyword arguments
# We can also send arguments with the key = value syntax
# This way the order of the arguments does not matter
def user_info(name, email, password):
    print(name, password, email)

user_info(email='george.miller@rediffmail.com', password='p@ssWord', name='George')


# Function with variable no of keyword arguments
def balls_played(**kwargs):
    return sum(kwargs.values())

print(balls_played(zeros=14, single=3, double=2, fours=4, sixes=1))


# Passing kwargs in a parametrized function
kwargs = {'name': 'Henry', 'email': 'henry.garcia@rediffmail.com.', 'phone': '8293129034'}
user_creation(**kwargs)
```

### Map, Filter, Reduce and Lambda Expressions

- Lambda functions/expressions are basically anonymous functions that can are created for one time
  usage
- Lambda functions are single line functions
- Lambda functions are mostly used as a parameter of another function

```python
import functools

# Simple function
def square(val):
    return val**2

# Lambda Expression of the previous function
sq = lambda val: val**2

print(square(12))
print(sq(15))

# Usage in map()
# Given a list of numbers, return another list containing the square of all the numbers of the initial list
numbers = [1, 2, 3, 4, 5]
print(list(map(square, numbers)))
print(list(map(lambda val: val**2, numbers)))

# Usage in filter()
# Given a list of numbers, return another list containing only even numbers from the initial list
print(list(filter(lambda val: val % 2 == 0, numbers)))

# Usage of reduce()
# Given a list of numbers, return the sum of all the numbers present in it
print(functools.reduce(lambda a, b: a + b, numbers))
```

### List Comprehensions

```python
# TODO: Create a new list of names having 5 characters without List Comprehension
names = ['Anadi', 'Shubham', 'Deep', 'Jyoti', 'Ankit', 'Barath', 'Vivek']
names_with_five_chars = []

for name in names:
    if len(name) == 5:
        names_with_five_chars.append(name)

print(names_with_five_chars)


# List Comprehension - simple version
# Copying all the names from one list to another (shallow-copy) with List Comprehension
names_copy = [name for name in names]
print(names_copy)

# List Comprehension with expression
names_length = [len(name) for name in names]
print(names_length)

# List Comprehension with condition
# TODO: Create a new list of names having 5 characters with List Comprehension
names_with_five_ch = [name for name in names if len(name) == 5]
print(names_with_five_ch)
```

### Modules

```python
# File: calc.py

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1 / num2

def multiply(num1, num2):
    return num1 * num2


# File: practice.py
# import calc
from calc import *

# print(calc.add(1, 2))
print(subtract(4, 2))
```

### random Module

```python
import random

# Choses a random value between 0 to 99
print(random.choice(range(100)))

# Choses a random value between A to Z
print(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

# Works equivalent to choice() function but does not actually build a range object
# Choses a random value between 0 to 99, with step=2
print(random.randrange(1, 99, 2))

# Generates a random value between 0 to 1
print(random.random())

# Shuffling the numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(numbers)
print(numbers)

# Seed can be used to control the randomness, so that every time the same random number is generated
# Once you set the seed to a value 10, random.random() will return the same random result in any system at any particular time
random.seed(10)
print(random.random())
```

### math Module

```python
import math

print(abs(-45))
print(math.fabs(-45))

print(math.ceil(1.12))
print(math.ceil(-45.18))

print(math.floor(1.12))
print(math.floor(-45.18))

print(math.pow(2, 3))
print(math.sqrt(16))
print(math.factorial(3))

print(math.pi)
print(math.lcm(2, 4, 12))
print(math.gcd(2, 4, 12))

print(min(43, 3, 92, 26))
print(max(43, 3, 92, 26))
```

### time, datetime and calendar Module

```python
# time module
import time

f_timestamp = time.time()
print(f_timestamp)

struct_time = time.localtime(f_timestamp)
print(struct_time)

str_time = time.asctime(struct_time)
print(str_time)


# day module
import calendar

# Prints the calendar of the given year
# print(calendar.calendar(2023))

# Prints the calendar of the given month
print(calendar.month(2023, 12))

# Returns the weekday of the given date
day_number = calendar.weekday(2023, 12, 4)
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
print(days[day_number])
```

### File Handling

```python
# Modes:
# r: open an existing file for a read operation
# w: open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well
# a:  open an existing file for append operation. It won’t override existing data
# r+:  To read and write data into the file. The previous data in the file will be overridden
# w+: To write and read data. It will override existing data
# a+: To append and read data from the file. It won’t override existing data
# Writing data into the file

# When a Python interpreter reads a Python file, it first sets a few special variables. Then it executes the code from the file. One of those variables is called __name__
# If the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value “__main__”
# If this file is being imported from another module, __name__ will be set to the module’s name. Module’s name is available as value to __name__ global variable
def main():
    fp = open('notepad.txt', 'w+')
    for i in range(1, 21):
        fp.write(f'This is line {i}\n')
    fp.close()

if __name__ == '__main__':
    main()


# Readine contents of the file
def main():
    fp = open('notepad.txt', 'r')

    if fp.mode == 'r':
        file_content = fp.read()
        print(file_content)

    fp.close()

if __name__ == '__main__':
    main()
```

### Exception Handling

```python
def main():
    try:
        fp = open('notepad1.txt', 'r')

        if fp.mode == 'r':
            file_content = fp.read()
        print(file_content)
    except IOError as e:
        print(f'ERROR: {e.args[1]}')
    else:
        fp.close()
        print('Task completed successfully')
    finally:
        print('Program execution finished')

if __name__ == '__main__':
    main()
```

### Object Oriented Programming in Python

#### Class, Constructors and Objects

```python
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class

# All classes have a function called __init__(), which is always executed when the class is being initiated
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created

# The __str__() function controls what should be returned when the class object is represented as a string
# If the __str__() function is not set, the string representation of the object is returned
class Phone:
    '''A simple class for test'''

    brand_name = 'Samsung'
    phone_version = 'S10'
    user_name = ''

    # Constructor
    def __init__(self, user_name):
        self.user_name = user_name

    def __str__(self):
        return f'{self.brand_name} - {self.phone_version} - {self.user_name}'

    def boot_logo(self):
        print(f'SAMSUNG {self.phone_version}')


my_phone = Phone('Deepjyoti Barman')
print(my_phone)                 # Samsung - S10 - Deepjyoti Barman
my_phone.boot_logo()            # SAMSUNG S10
print(my_phone.__doc__)         # A simple class for test
del my_phone
```

#### Getters and Setters

```python
class Phone:
    brand_name = 'Samsung'
    model = 'S10+'

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = self.model + f' {model}'

    # Constructor
    def __init__(self, user_name):
        self.user_name = user_name

    def __str__(self):
        return f'{self.brand_name} - {self.model}'


my_phone = Phone('Deepjyoti Barman')
print(my_phone)
print(my_phone.get_model())
my_phone.set_model('Ultra Pro Max')
print(my_phone.get_model())
```

#### Inheritance and super() method

```python
class Samsung:
    def __init__(self):
        print('I am Samsung')

    def make_screen(self):
        print('I make screens')

    def samsung_test(self):
        print('Screen test 1: OK')
        print('Screen test 2: OK')
        print('Screen test 3: OK')


class IPhone(Samsung):
    def __init__(self):
        super().__init__()
        print('I am IPhone')

    def make_processor(self):
        print('I make A10 Bionic processors')

    def iphone_test(self):
        print('A10 processor test: OK')
        super().samsung_test()


my_phone = IPhone()             # I am Samsung \n I am IPhone
my_phone.make_processor()       # I make A10 Bionic processors
my_phone.make_screen()          # I make screens
my_phone.iphone_test()          # A10 processor test: OK \n Screen test 1: OK \n Screen test 2: OK \n Screen test 3: OK
```

#### Method Overriding

```python
class Samsung:
    def __init__(self):
        print('I am Samsung')

    def make_screen(self):
        print('Samsung: I make screens')


class IPhone(Samsung):
    def __init__(self):
        super().__init__()
        print('I am IPhone')

    def make_screen(self):
        print('IPhone: I make screens')


my_phone = IPhone()         # I am Samsung \n I am IPhone
my_phone.make_screen()      # IPhone: I make screens
```

### Database - sqlite3 database

```python
# File: db_helper.py
import sqlite3

db_name = 'my_todo.db'
table_name = 'tasks'
connection = sqlite3.connect(db_name)
cursor = connection.cursor()


def create_table():
    sql = f'CREATE TABLE IF NOT EXISTS {table_name} (\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
        taskname TEXT\
    )'
    cursor.execute(sql)


def data_entry(task):
    cursor.execute(f'INSERT INTO {table_name} (taskname) VALUES (?)', [task])
    connection.commit()
    print('Task is added in the database')


def print_data():
    sql = f'SELECT * FROM {table_name}'
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row[0], '--->', row[1])


def delete_task(index):
    cursor.execute(f'DELETE FROM {table_name} WHERE id = ?', [index])
    print('Task is deleted from the database')


def close_connection():
    cursor.close()
    connection.close()


# File: runner.py
import db_helper


def main():
    run = True
    db_helper.create_table()

    while run:
        print('\n')
        print('1. Insert new task in TODO list \n')
        print('2. View the TODO list \n')
        print('3. Delete the task from the TODO list \n')
        print('4. Exit\n')

        selector = input('Choose any of the above options: ')

        if selector == '1':
            task = str(input('Enter the task: '))
            db_helper.data_entry(task)
        elif selector == '2':
            db_helper.print_data()
        elif selector == '3':
            index_to_delete = input('Enter the index of the task to delete: ')
            db_helper.delete_task(index_to_delete)
        elif selector == '4':
            run = False
        else:
            print('Please choose a valid option')
    db_helper.close_connection()


if __name__ == '__main__':
    main()
```

### Iterators and Generators

```python
import random

# Anything that can generate an iterator is an generator
# Following is a generator function that returns a iterable generator object of 6 integers
def magic_number_generator():
    for i in range(6):
        yield random.randint(0, 10)


# Converting the iterable generator object to list
print(list(magic_number_generator()))
print()

# Printing all the objects of the iterable generator object
for num in magic_number_generator():
    print(num, end=' ')
print()
```
