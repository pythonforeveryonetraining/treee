# Treee

This package was created to help me visualize directory structures in my coding tutorials. There are many ASCII tree visualizers available but this one adds two features I needed:

- Sort alphabetically but first by directories, then by files
- Exclude directories from output

Example:

```
dirtree/
├── dist/
│   ├── treee-1.0.0-py3-none-any.whl
│   └── treee-1.0.0.tar.gz
├── src/
│   └── treee/
│       └── tree.py
├── .gitignore
├── LICENSE.txt
├── README.md
└── pyproject.toml
```

## Install

```
pip install treee
```

Visit project on [PyPI](https://pypi.org/project/treee)

## Features

- Shows ASCII tree of current folder and beyond
- Sorts by type (folders on top), then by name
- Supports excluding of directories
- Can be run from terminal or imported in Python code

## Import in exising code

```
from dirtree import tree

tree.print_tree()
```

## Run from command line

```
treee
```

## Exclude files

Create file `.dirtree-ignore` in the directory where treee is executed.

Example of ignored directories:

```
env
__pycache__
*egg*
.git
```
