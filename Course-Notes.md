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

## Week2
