# [TEST] Python Design Wizard docs

## Introduction

This part of the documentation will help you to create any test in a few steps. Each step must be followed as descripted, otherwise the Python Design Wizard will not function properly.
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

`self`: is an modified argument with test assertation and also the `PDW` injected as an attribute. 

When done, the file should be like bellow.

Example: `test_xpto.py`
```python
def test_xpto(self):
    self.assertTrue(True)
```

### Methods

#### design_populate_all_entities

🚧 under construction 🚧

#### design_populate_loop_entities

🚧 under construction 🚧

#### design_get_relations_from_entity

🚧 under construction 🚧

#### design_get_callees_from_entity_relation

🚧 under construction 🚧

#### design_entity_has_type_as_child

🚧 under construction 🚧

#### design_list_entity_has_every_child_as_type

🚧 under construction 🚧

#### design_list_entity_has_some_child_as_type

🚧 under construction 🚧

#### design_get_qtd_calls_function

🚧 under construction 🚧

#### design_populate_all_entities

🚧 under construction 🚧

