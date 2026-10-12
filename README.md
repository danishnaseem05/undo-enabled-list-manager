# Undo-Enabled List Manager

This is a simple list Manager backed by MyLinkedList, with undo functionality backed by MyStack. Interfacing is available through public python methods and a CLI through `cli.py`

## ListManager Methods

- `add(item, index)` — inserts a task at an index.
- `remove(index)` — removes a task.
- `edit(index, new_data)` — changes a task's description.
- `move(from_pos, to_pos)` — moves a task to another index.
- `clear()` — removes all tasks and can be reversed with `undo()`.
- `undo()` — reverses the most recent change.
- `get_items()` — returns all task descriptions as a list.
- `is_empty()` — returns whether the list is empty.
- `get_count()` — returns the number of tasks.
- `__str__()` — enables `print()` and `str()` for the list manager.

## CLI

Run the CLI from the project directory:

```bash
python3 cli.py
```

Available commands:

```text
add <INDEX> <DESCRIPTION>
remove <INDEX>
edit <INDEX> <DESCRIPTION>
move <FROM_INDEX> <TO_INDEX>
list
clear
undo
help
quit
```

