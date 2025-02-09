from pathlib import Path
import re
import fnmatch

def matches(patterns, name):
    for p in patterns:
        if fnmatch.fnmatch(name, p):
            return True
    return False

def get_flat_tree(folder, ignore, indent=""):
    if indent == "":
        yield f"{folder.name}/"

    # load dir and exclude unwanted files
    filtered = [i for i in folder.iterdir() if not matches(ignore, i.name)]

    # Load directory items and sort them, first by type (folders on top), then by name.
    sorted_items = [i for i in sorted(filtered, key=lambda path: (not path.is_dir(), path.name))]

    # Turn items into a list of tuples where the first tuple element marks a regular node or an end node.
    connected_items = [("├── " if i < len(sorted_items) - 1 else "└── ", x) for i, x in enumerate(sorted_items)]

    for connector, path in connected_items:
        if path.is_dir():
            yield f"{indent}{connector}{path.name}/"
            if connector == "├── ":
                yield from get_flat_tree(path, ignore, indent + "│   ")  # Node must be followed down by a vertical line.
            else:
                yield from get_flat_tree(path, ignore, indent + "    ")  # End node must be followed by empty space.
        else:
            yield f"{indent}{connector}{path.name}"

def print_tree():
    path = Path.cwd()
    ignore = [".treee-ignore"]
    try:
        with open(path.joinpath(".treee-ignore"), "r") as file:
            ignore += file.read().strip().split()
    except:
        pass  # could not load config file. Ignore error.

    print(f"Ignoring: {ignore}.")
    for x in get_flat_tree(path, ignore):
        print(x)
