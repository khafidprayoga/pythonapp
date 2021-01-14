# About
This a simple app that parsing computer number (binary, decimal, octal, and hexadecimal).  
Tested with Python 3.9 and 3.7 working perfectly.

# How To Install
This app is built with Click (CLI builder), so all command handle by it.
You can install through a few steps below, because i have create setup.py.
Before follow installing instructions, make sure you have to clone **pythonapp** repository, and
**change directory to kalkulator-it**

1. Create a virtual environment  
    ```python -m venv env```
2. Activate the environment  
    ```source env/bin/activate```
3. Install this app as module  
    ```pip install --editable .```

# How To Use
The idea is simple, this app need two options and one argument.  
The options are:
1. "-s" or "--source"
2. "-d" or "--destination"

You should fill it, with valid parameters (bin, dec, oct, hex), and finally put your number as an argument.

Example :  
I want to convert "7" from decimal to binary.  
```calculate -s dec -d bin 7```  
Output:  
```Result	: 111```  
For more information you can use ```calculate --help```.  