JSON Merge Patch Library
==============================================

This library provides functions to merge json in accordance with https://tools.ietf.org/html/rfc7386

-------------
Install using pip:
```
pip install json-merge-patch
```

Or you can clone the repository and paste:
```
python setup.py install
```
or for development use:
```
python setup.py develop
```
This requires setuptools to be installed.
It has no dependencies outside the stadard library so no pip requirements files are needed. 

To test run:
```
python -m unittest discover
```

Usage as a library
------------------

The library does not deal with json loading and dumping that is up to the user.

There are two functions:

**merge:** Takes a list of input dictionaries and merges them in turn.

**create_patch:** Takes 2 dictionaries the original and the target and gives you the minimal patch needed to go from the original to the target.  So if merge(a, b) == c then create_patch(a, c) == b.

Merge example
```
import json_merge_patch

input1 = {"a": 1}
input2 = {"a": 2, "b": 3}

result = json_merge_patch.merge(input1, input2)

print(result)
# {'a': 2, 'b': 3}
```


Create Patch example
```

input1 = {"a": 1}
results = {'a': 2, 'b': 3}

patch = json_merge_patch.create_patch(input1, result)
print(patch)
# {'a': 2, 'b': 3}
```

Merge example preserving order. Inputs need to be OrderedDicts. Will error otherwise.
Argument "position" can either be 'first', 'last'.

```
import json_merge_patch

input1 = OrderedDict([("a", 1)])
input2 = OrderedDict([("a", 1), ("b", 3)])

result = json_merge_patch.merge(input1, input2, position="first")
print(result)
# {'b': 3, 'a': 2}
```

Usage as a command line tool
----------------------------

Has two functions

```
json-merge-patch merge input1.json input2.json 

json-merge-patch create-patch original.json target.json 
```

By default results are printed to stdout. If you use the -o flag they can be saved to a file.

```
json-merge-patch merge input1.json input2.json -o output.json

json-merge-patch create-patch original.json target.json -o patch.json
```

More can be found at:

```
json-merge-patch merge --help

json-merge-patch create-patch --help
```
