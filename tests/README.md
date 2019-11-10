# [TEST] Python Design Wizard docs

## Introduction

This part of the documentation will help you to create any design test in a few steps. Each step must be followed as descripted, otherwise the Python Design Wizard will not function properly.
To use the [demo](https://github.com/Caio-Batista/python-dw#running-demo-interact) version of the CLI, follow the instructions in the main documentation, then it should be all setup to run the tests created using this section.

### 1. Explore the API

First of all, to create any test using this software, one should be familiarized with the [Python Design Wizard API](https://github.com/Caio-Batista/python-dw/tree/master/api#api-python-design-wizard-docs)


### 2. Creating the py file

Create an empty file `test_{name of your test}.py`

Example:
```shell
$ touch test_xpto.py
```

### 3. Write a template test

Inside your test file write a simple test passing a self argument and with **the exact name of your file**

`self`: is an modified argument with test assertation and also the `dw` (*Design Wizard*) injected as an attribute. 

When done, the file should be like bellow.

Example: `test_xpto.py`
```python
def test_xpto(self):
    self.assertTrue(True)
```

### 4. Initialize PDW entities

**ALL TESTS** must start with the initialization of the entities node, then the *Python Design Wizard* can recognize each node as a variable and use them as object to tests.

`dw`: This attribute is the *Python Design Wizard* injected in the self test object, it contains all the [API](https://github.com/Caio-Batista/python-dw/tree/master/api#api-python-design-wizard-docs) needed to create design tests.

The test files should be alike in the first line.

Example: `test_xpto.py`
```python
def test_xpto(self):
    self.dw.design_populate_all_entities()
    self.assertTrue(True)
```

### 5. Use the API and the rightful assertations

Erase the dummy assert and now create the real test using the [API](https://github.com/Caio-Batista/python-dw/tree/master/api#api-python-design-wizard-docs). This example bellow just check if the function `print` is called more than once in the code. 

Example: 

`test_xpto.py`
```python
def test_xpto(self):
    self.dw.design_populate_all_entities()
    self.assertTrue(
        self.dw.design_get_qtd_calls_function('print') > 0
    )
```

`file_to_be_tested.py`
```python
print('this')
print('design')
print('test')
print('should')
print('pass')
```

### 6. Where should I place my test?

🚧 under construction 🚧

