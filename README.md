# Python Design Wizard

## Requiriments

### Python version over version 2.x
This version of Python Design Wizard uses (mainly) the [AST](https://docs.python.org/2/library/ast.html) api from the Python 2.x lib. It also runs with the [3.x version](https://docs.python.org/3.5/library/ast.html) of the api, but it was not the focus of this project so it may have some issues in some cases e.g.: Print, dict and calls entities.  

## Introduction 

### What is it?
The Python Design Wizard is a tool, and also an api, that uses the AST (Abstract syntax tree) of Python to find anti-patterns or *violations* in Python programs without having to run them in anyway. An example of AST in python:

![alt text](http://garethrees.org/2011/07/17/grammar/binop.png)

### Why should I use it?
First of all, this tool is way easier to use than the raw AST, that has some very useful options, but need abstraction to be used in different ways. The Python DW uses two forms of abstractions that are Relation and Entity. These two allow the user to search for patterns, check the tree for calls of specific functions and also to restrict the use of them too.  
Python DW can also be used to search slow algorithms based on their syntax. It comes along with an interactive module to execute your own *Design tests*, called [dw-check](https://github.com/Caio-Batista/python-dw#what-is-the-dw-check).

### How to use the API?
This tool is used like any api else. It creates the abstractions with side functions in the main module that can be found in [here](https://github.com/Caio-Batista/python-dw/blob/master/api/design_wizard.py). All the functions have their own documentations but are self explanned by their names and the section of the code that are found.

Next is an example how to use the tool:

```python
from api.design_wizard import PythonDW

python_dw = PythonDW()
python_dw.parse("path/to/file.py")
```
After this you can use the functions to create whatever restrictions or rule search that you want.

### What is the dw-check?
The **dw-check** is an interactive module that helps the user to filter functions and run tests of syntax using the api of Python DW, for all Python files in a certain directory. With a detailed command line interface, the user can create their own scripts with tests without having to create a class test or implement searching algorithms using the api. Those two things are already implemented with this module.

To get in to how to use the **dw-check**, see the [section bellow](https://github.com/Caio-Batista/python-dw#how-to-use-the-dw-check) or just run the following command:

```shell
$ ./dw-check help
```

### How to use the dw-check?
To make it easier to understand, this section will be divided in two parts (for each purpose), function restriction and script testing. 

#### Function restriction
This part of the **dw-check** uses the api to search for a costumizable group of functions through a directory for each Python file present in it. To use it is really simple, the only setup needed is a **json** file containing the functions to be found. Like bellow:

```shell
$ ./dw-check -f my/dir/functions.json -d my/dir/python_files/
```
**-f** stands for "functions" and **-d** stands for "directory".

In order for the **dw-check** to work properly the json file must be in this format, for the N funtions that the user wants to filter: 

```json
{"functions_not_allowed":["function1", "function2"]}
```
The result will be displayed as it follows:

```shell
$ ./dw-check -f path/dir/functions.json -d path/dir/python_files_dir

Directory: path/dir/python_files_dir

.  file1.py
function1 file2.py
function2 file3.py
function1 function2 file4.py

$
```
For each file in the directory will be printed the result. The dot (".") represents that for this file there's none of the functions, and if exists any of these functions in the file, the result will be the functions fould and then the file name.


#### Script testing
This part of the **dw-check** uses the api to incorporate the users' tests to the Python DW, it is very similar to the function restriction functionality, but this time instead of having a json file with the functions, here it's a json file containing the name of the files (scripts) with test case functions. To use this feature run:

```shell
$ ./dw-check -s path/dir/scripts.json -d path/dir/python_files_dir
```

Here **-s** stands for "scripts" and again **-d** stands for "directory".


In order for the **dw-check** to work properly the json file must be in this format, for the N scripts that the user wants to filter: 

```json
{"scripts":["script1.py", "script2.py"]}
```

And the scrips must be like this:

- **test.py**
```python
def test(self):
    self.assertEqual(self.dw.get_all_classes_str(), \
     ['Test','Test2'])
    self.assertEqual(self.dw.get_all_functions_str(), \
     ['func1','func2', 'inside_func'])
    self.assertEqual(self.dw.get_all_imports_str(), \
     ['Math','unittest'])
```
**dw** is the current Design Wizard that already parsed the file to be tested and with all the api functionalities.

To incorporate the test into Python DW the test case must start with the prefix **test** and that's why the json file and the functions are similar to the following:

```json
{"scripts":["test_case_1.py","test_case_2.py"]}
```

The result of the command:

```shell
$ ./dw-check -s path/dir/scripts.json -d path/dir/python_files_dir

Directory: path/dir/python_files_dir

. . file1.py
test_case_1 . file2.py
test_case_1 test_case_2 file3.py
. test_case_2 file4.py

$
```
For each one of the files all the scripts are tested, if the file passes the test then the dot (".") will be shown, otherwise the name of the test case will appear. Different from the function restriction, this result will print one dot for each test passed even if the file passes all tests. 

---
**NOTE 1**

In order to **dw-check** work properly the script file name **must be the same** name of the test case inside of it.

---

---
**NOTE 2**

Also in order to **dw-check** work properly the script file **must be placed** in this [directory](https://github.com/Caio-Batista/python-dw/tree/master/tests/scripts) (tests/scripts). Notice here that the directory already has a file, **DO NOT ERASE test_selected_scripts.py**. This file is essential to the execution of the test suite.

---

### Is it tested?
Python DW has 100% of coverage in function testing, this tests can be found in the [test directory](https://github.com/Caio-Batista/python-dw/tree/master/tests). This tool is also self-tested, what means that the code tests itself with the abstract syntax tree. 
The test suite can be improved anytime by the user who can add new kinds of tests like *Design Tests*.

To execute the tests already developed just run the command:

```shell
$ ./run_tests.sh
```
The result of the command is a well detaled test suite run of each module of the tool. 

---

### Running Demo interact
Use the following commands in order to use the demo script, the three commands are listed here with optional parameters, running as restricted functions or scrips.

The parameter `t` here is the recursive directory flag.
Use `""` to pass a parameter as null.

Just restricted functions:

```shell
python -m demo.demo_interact demo/restricted.json {{path/to/folder}} "" t
```

Just scripts (Design tests):

```shell
python -m demo.demo_interact "" {{path/to/folder}} demo/scripts.json t
```

Both restrictions:

```shell
python -m demo.demo_interact demo/restricted.json {{path/to/folder}} demo/scripts.json t
```

## Examples and sample data
The Python DW comes with an example of what you can do with this api. With this files th user can understand the concept of *Design testing* and also have samples of data and scripts to run along with **dw-check**.
Listed bellow are the files that can be used as models/guides or tests it self.

- [functions restrict json sample](https://github.com/Caio-Batista/python-dw/blob/master/demo/restrict.json)
- [scripts to test json sample](https://github.com/Caio-Batista/python-dw/blob/master/demo/scripts.json)
- [scripts sample](https://github.com/Caio-Batista/python-dw/tree/master/tests/scripts/samples)
- [python modules sample](https://github.com/Caio-Batista/python-dw/tree/master/data)
- [python modules divided by single entity](https://github.com/Caio-Batista/python-dw/tree/master/tests/data)

## Some important definitions

### Design Tests

### Violations

