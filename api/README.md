# [API] Python Design Wizard docs

## Introduction 

### What is this API?

This documentation explains detailed every major design test API method. Here it can be found every `source code`, `parameter` and `return` for each method.

### Basic concepts

In order to use correctly the API one needs to understand the basic concept about tree abstraction that comes along with *Python Design Wizard*.

Every usage of this API starts parsing the Python file to be extracted the AST and then populate the *Python Design Wizard* with all the nodes, now known as entities.

Each entity has an amount of relations with one or more entities.

All entities inside `entities` dict in *Python Design Wizard* object, except for functions, have value as an array of entities. The key is always a string containing the name of the node.

In order to organize multiple entities with same name, the number in order of appearence is concated after each name of function.

Example:
```
{
    "for": [
        {name: "for1", ...},
        {name: "for2", ...}
    ]
}
```

### Methods

#### design_populate_all_entities

This method start all design tests, it parses the AST nodes into a single dict containing all entities with their respective relations.

##### Parameters

`None`

##### Return

`None`

##### Example

`file.py`
```python
print('Hello world!') # <print1>
```

`api_example.py`
```python
from api.design_wizard import PythonDW

python_dw = PythonDW()
python_dw.parse("path/to/file.py")
python_dw.design_populate_all_entities()
# dw is populated now
```

`python_dw.entities`
```
{
    "print": [<print1>]
}
```

---

#### design_populate_loop_entities

Same principle of the last method but here it will be parsed only loops. This method is very useful if one wants to create design tests regarding just performance.

##### Parameters

`loop_name`: Can be `while` or `for` (default) the two types of loop in Python.

##### Return

`None`

##### Example

`file.py`
```python
for e in [1,2,3]:
    print(e + 1)
```

`api_example.py`
```python
from api.design_wizard import PythonDW

python_dw = PythonDW()
python_dw.parse("path/to/file.py")
python_dw.design_populate_loop_entities()
# dw is populated now
```

`python_dw.entities`
```
{
    "for": [<for1>]
}
```

---

#### design_get_entity

This method gets the entity parsed by it's name. Always returns an array because *Python Design Wizard* assumes the overload of nodes with same name. E.g.: `for`, `while`, `if`.

##### Parameters

`name`: Name of the entity

##### Return

Array of entities

##### Example

`file.py`
```python
print('Hi there!')
```

`api_example.py`
```python
from api.design_wizard import PythonDW

python_dw = PythonDW()
python_dw.parse("path/to/file.py")
python_dw.design_populate_loop_entities()
# dw is populated now
python_dw.design_get_entity('print')
# Output -> [<print1>]
```

`python_dw.entities`
```
{
    "print": [<print1>]
}
```

---

#### design_get_relations_from_entity

This method gets the array of a single type of relation from an entity.

##### Parameters

`entity_name`: Name of the entity
`type_relation`: Can be any value of [these](https://github.com/Caio-Batista/python-dw/tree/master/api#types-of-relations)

##### Return

Array of relations

##### Example

`file.py`
```python
for e in [1,2,3]:
    for letter in 'abc':
        print(letter)
```

`api_example.py`
```python
from api.design_wizard import PythonDW

python_dw = PythonDW()
python_dw.parse("path/to/file.py")
python_dw.design_populate_all_entities()
# dw is populated now
python_dw.design_get_relations_from_entity('for1', 'HASLOOP')
# Output -> [<Relation_for1_for2>]
```

`python_dw.entities`
```
{
    "for": [<for1>, <for2>],
    "print": [<print1>]
}
```

---

#### design_get_callees_from_entity_relation

This method gets the array of a entities that are the endpoint from a single relation.

##### Parameters

`entity_name`: Name of the entity
`type_relation`: Can be any value of [these](https://github.com/Caio-Batista/python-dw/tree/master/api#types-of-relations)

##### Return

Array of entities

##### Example

`file.py`
```python
for e in [1,2,3]:         # <for1>
    for letter in 'abc':  # <for2>
        print(letter)     # <print1>
```

`api_example.py`
```python
from api.design_wizard import PythonDW

python_dw = PythonDW()
python_dw.parse("path/to/file.py")
python_dw.design_populate_all_entities()
# dw is populated now
python_dw.design_get_callees_from_entity_relation('for1', 'HASLOOP')
# Output -> [<for2>]
```

`python_dw.entities`
```
{
    "for": [<for1>, <for2>],
    "print": [<print1>]
}
```
---

#### design_entity_has_type_as_child

This method verifies if the entity has any child node as a specific AST type. All the types of AST nodes can be found [here](https://greentreesnakes.readthedocs.io/en/latest/nodes.html).

##### Parameters

`entity`: Desgin entity object
`type_to_filter`: Any of the AST node types

##### Return

Boolean value

##### Example


`file.py`
```python
for e in [1,2,3]:
    a = e
```

`api_example.py`
```python
from api.design_wizard import PythonDW

python_dw = PythonDW()
python_dw.parse("path/to/file.py")
python_dw.design_populate_all_entities()
# dw is populated now
entity_for = python_dw.design_get_entity('for')
# entity_for == [<for1>]
python_dw.design_entity_has_type_as_child(entity_for[0], 'assign')
# Output -> True
```

`python_dw.entities`
```
{
    "for": [<for1>],
    "assign": [<assign1>]
}
```

---

#### design_list_entity_has_every_child_as_type

Same behavior of the previous method but applied to a list of nodes. Verifying if every element of the list is the type passed as a parameter.

##### Parameters

`entity_list`: Desgin entity object array
`type_to_filter`: Any of the AST node types

##### Return

Boolean value

##### Example

`file.py`
```python
for e in [1,2,3]:   # <for1>
    a = e           # <assign1>
    print('foo')    # <print1>
```

`api_example.py`
```python
from api.design_wizard import PythonDW

python_dw = PythonDW()
python_dw.parse("path/to/file.py")
python_dw.design_populate_all_entities()
# dw is populated now
entity_for = python_dw.design_get_entity('for')
# entity_for == [<for1>]
python_dw.design_list_entity_has_every_child_as_type(entity_for, 'assign')
# Output -> False
```

`python_dw.entities`
```
{
    "for": [<for1>],
    "assign": [<assign1>],
    "print": [<print1>]
}
```

---

#### design_list_entity_has_some_child_as_type

Same behavior of the previous method but applied to a list of nodes. Verifying if any element of the list is the type passed as a parameter.


##### Parameters

`entity_list`: Desgin entity object array
`type_to_filter`: Any of the AST node types

##### Return

Boolean value

##### Example

`file.py`
```python
for e in [1,2,3]:
    a = e
    print('foo')
```

`api_example.py`
```python
from api.design_wizard import PythonDW

python_dw = PythonDW()
python_dw.parse("path/to/file.py")
python_dw.design_populate_all_entities()
# dw is populated now
entity_for = python_dw.design_get_entity('for')
# entity_for == [<for1>]
python_dw.design_list_entity_has_every_child_as_type(entity_for, 'assign')
# Output -> True
```

`python_dw.entities`
```
{
    "for": [<for1>],
    "assign": [<assign1>],
    "print": [<print1>]
}
```

---

#### design_get_qtd_calls_function

This method gets the quantity of function calls in all the parsed tree.

##### Parameters

`name`: Function name

##### Return

Integer

##### Example

`file.py`
```python
for e in [1,2,3]:
    print(e)
```

`api_example.py`
```python
from api.design_wizard import PythonDW

python_dw = PythonDW()
python_dw.parse("path/to/file.py")
python_dw.design_populate_all_entities()
# dw is populated now
entity_for = python_dw.design_get_entity('for')
# entity_for == [<for1>]
python_dw.design_get_qtd_calls_function('print')
# Output -> 1
```

`python_dw.entities`
```
{
    "for": [<for1>],
    "print": [<print1>]
}
```

---

### Types of relations

| Relation | Description | Reverse relation |
|---|---|---|
| DEFINES | - | ISDEFINED |
| ISDEFINED | - | DEFINES |
| CONTAINS | - | ISCONTAINED |
| ISCONTAINED | - | CONTAINS |
| HASFIELD | - | ISFIELDOF |
| ISFIELDOF | - | HASFIELD |
| CALLS | - | ISCALLED |
| ISCALLED | - | CALLS |
| HASLOOP | - | ISLOOPOF |
| ISLOOPOF | - | HASLOOP |


### Types of node's abstraction (entities)

| Entity |
|---|
| Loop |
| Function |
| Field |
| Class |
| Import |
| Parameter |



