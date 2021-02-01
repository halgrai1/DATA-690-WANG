# Hala Algrain's DATA 690 Course Notes

## Week 1
### In-Class Notes 1.28.2021
**Intro**

- Every github repository has a README file that explains the project.
- The github document format is called markdown “.md”
- Deepnote uses virtual machine to run code
- notebooks have cells with either code, text, or sql
- Cells that are text can be edited; see [cheat sheet](https://www.markdownguide.org/cheat-sheet/) ; these cells are markdowns
- .ipynb = interactive python notebook ; it's a jupytr notebook
- .py is a python program


**Code**
`pwd` to know present working directory

`ls` 

Create a terminal in deepnote > run the program e.g. hello.py

`vi hello.py` file : allows you to edit from terminal .py without a user interface like the jupyter notebook environment

`gip` need to double check what that is


**Prof's Advice**
1. He recommends wc3 tutorial on link on his github.
2. Learn to use the virtual machine.


### Chapter 1 Notes
- Python is very versatile but has limitations like when creating "highly concurrent, multithreaded
applications".
- There are many kinds of data, e.g. time series, matrices, and tabular (spreadsheets)
- There are many kinds of Pythong Libraries, e.g. pandas, NumPy, matplotlib
- Python 3 is the most up-to-date version


### Chapter 2 Notes

**Python Interpreter**
`python` runs python in terminal
- differences between standard terminal Python interpreter, ipython shell, and Jupyter notebook and how to run them.

**Keyboard Shortcuts**
- Ctrl-P or up-arrow Search backward in command history for commands starting with currently entered text
- Ctrl-N or down-arrow Search forward in command history for commands starting with currently entered text
- Ctrl-R Readline-style reverse history search (partial matching)
- Ctrl-Shift-V Paste text from clipboard
- Ctrl-C Interrupt currently executing code
- Ctrl-A Move cursor to beginning of line
- Ctrl-E Move cursor to end of line
- Ctrl-K Delete text from cursor until end of line
- Ctrl-U Discard all text on current line
- Ctrl-F Move cursor forward one character
- Ctrl-B Move cursor back one character
- Ctrl-L Clear screen

**Magic Commands**
Special commands (which are not built into Python itself) are known as “magic” commands. A magic command is any command prefixed by the percent symbol %
- %quickref Display the IPython Quick Reference Card
- %magic Display detailed documentation for all of the available magic commands
- %debug Enter the interactive debugger at the bottom of the last exception traceback
- %hist Print command input (and optionally output) history
- %pdb Automatically enter debugger after any exception
- %paste Execute preformatted Python code from clipboard
- %cpaste Open a special prompt for manually pasting Python code to be executed
- %reset Delete all variables/names defined in interactive namespace
- %page OBJECT Pretty-print the object and display it through a pager
- %run script.py Run a Python script inside IPython
- %prun statement Execute statement with cProfile and report the profiler output
- %time statement Report the execution time of a single statement
- %timeit statement Run a statement multiple times to compute an ensemble average execution time; useful for timing code with very short execution time
- %who, %who_ls, %whos Display variables defined in interactive namespace, with varying levels of information/ verbosity
- %xdel variable Delete a variable and attempt to clear any references to the object in the IPython internals

**Python Language Basics**
- Python typically have both attributes (other Python objects stored “inside” the object) and methods (functions associated with an object that can have access to the object’s internal data). Both of them are accessed via the syntax `obj.attribute_name`
- Duck typing: Often you may not care about the type of an object but rather only whether it has certain methods or behavior

**List of Binary Operators**
- a + b Add a and b
- a - b Subtract b from a
- a * b Multiply a by b
- a / b Divide a by b
- a // b Floor-divide a by b, dropping any fractional remainder
- a ** b Raise a to the b power
- a & b True if both a and b are True; for integers, take the bitwise AND
- a | b True if either a or b is True; for integers, take the bitwise OR
- a ^ b For booleans, True if a or b is True, but not both; for integers, take the bitwise EXCLUSIVE-OR
- a == b True if a equals b
- a != b True if a is not equal to b
- a <= b, a < b True if a is less than (less than or equal) to b
- a > b, a >= b True if a is greater than (greater than or equal) to b
- a is b True if a and b reference the same Python object
- a is not b True if a and b reference different Python objects

**Standard Python Scalar Types**
- None The Python “null” value (only one instance of the None object exists)
- str String type; holds Unicode (UTF-8 encoded) strings
- bytes Raw ASCII bytes (or Unicode encoded as bytes)
- float Double-precision (64-bit) floating-point number (note there is no separate double type)
- bool A True or False value
- int Arbitrary precision signed integer

**Strings**
- String objects have a format method that
can be used to substitute formatted arguments into the string, producing a new
string:
`In [74]: template = '{0:.2f} {1:s} are worth US${2:d}'`
In this string,
  -  {0:.2f} means to format the first argument as a floating-point number with two
decimal places.
  -  {1:s} means to format the second argument as a string.
  - {2:d} means to format the third argument as an exact integer.
- To substitute arguments for these format parameters, we pass a sequence of arguments
to the format method:
  - `In [75]: template.format(4.5560, 'Argentine Pesos', 1)`
  - `Out[75]: '4.56 Argentine Pesos are worth US$1'`
  
  **Date and Time Format Specificatins**
- %Y Four-digit year
- %y Two-digit year
- %m Two-digit month [01, 12]
- %d Two-digit day [01, 31]
- %H Hour (24-hour clock) [00, 23]
- %I Hour (12-hour clock) [01, 12]
- %M Two-digit minute [00, 59]
- %S Second [00, 61] (seconds 60, 61 account for leap seconds)
- %w Weekday as integer [0 (Sunday), 6]
- %U Week number of the year [00, 53]; Sunday is considered the first day of the week, and days before the first Sunday of
the year are “week 0”
- %W Week number of the year [00, 53]; Monday is considered the first day of the week, and days before the first Monday of
the year are “week 0”
- %z UTC time zone offset as +HHMM or -HHMM; empty if time zone naive
- %F Shortcut for %Y-%m-%d (e.g., 2012-4-18)
- %D Shortcut for %m/%d/%y (e.g., 04/18/12)

## Week2
