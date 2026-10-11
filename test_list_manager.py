
"""
Author:
Date:

Purpose:

Input:

Output:
"""

from list_manager import ListManager


def format_header(header):
    print(f"\n################## {header} ##################\n")


def main():
    format_header("Initialize empty list manager")
    list_manager = ListManager()
    print(f"Is list manager empty? | Expected: True | Actual: {list_manager.is_empty()}")
    print(f"Length of tasks stored | Expected: 0 | Actual: {list_manager.get_count()}")

    format_header("Testing add")
    list_manager.add("Study for exam 2", 0)
    list_manager.add("Pay electric bill", 1)
    list_manager.add("Back up photos", 2)
    list_manager.add("Read 10 pages", 3)
    list_manager.add("Cancel unused subscription", 4)
    print(f"Added todos to list manager")
    print(f"Is list manager empty? | Expected: False | Actual: {list_manager.is_empty()}")
    print(f"Lenght of list manager | Expected: 5 | Actual: {list_manager.get_count()}")
    print(f"Items in list manager | Expected: ['Study for exam 2', 'Pay electric bill', 'Back up photos', 'Read 10 pages', 'Cancel unused subscription'] | Actual: {list_manager.get_items()}")
    print()
    list_manager.undo()
    print(f"Called Undo")
    print(f"Lenght of list manager | Expected: 4 | Actual: {list_manager.get_count()}")
    print(f"Items in list manager | Expected: ['Study for exam 2', 'Pay electric bill', 'Back up photos', 'Read 10 pages'] | Actual: {list_manager.get_items()}")

    format_header("Testing edit")
    list_manager.edit(3, "Read the entire chapter")
    print(f"Items in list manager | Expected: ['Study for exam 2', 'Pay electric bill', 'Back up photos', 'Read the entire chapter'] | Actual: {list_manager.get_items()}")
    print()
    list_manager.undo()
    print(f"Called Undo")
    print(f"Items in list manager | Expected: ['Study for exam 2', 'Pay electric bill', 'Back up photos', 'Read 10 pages'] | Actual: {list_manager.get_items()}")

    format_header("Testing move")
    list_manager.move(0, 2)
    print(f"Moved task at index 0 to index 2 | Expected: ['Pay electric bill', 'Back up photos', 'Study for exam 2', 'Read 10 pages'] | Actual: {list_manager.get_items()}")
    print()
    list_manager.undo()
    print(f"Called Undo")
    print(f"Items in list manager | Expected: ['Study for exam 2', 'Pay electric bill', 'Back up photos', 'Read 10 pages'] | Actual: {list_manager.get_items()}")

    format_header("Testing remove")
    list_manager.remove(1)
    print("Removed task at index 1")
    print(f"Lenght of list manager | Expected: 3 | Actual: {list_manager.get_count()}")
    print(f"Items in list mananger | Expected: ['Study for exam 2', 'Back up photos', 'Read 10 pages'] | Actual: {list_manager.get_items()}")
    print()
    list_manager.undo()
    print(f"Called Undo")
    print(f"Lenght of list manager | Expected: 4 | Actual: {list_manager.get_count()}")
    print(f"Items in list manager | Expected: ['Study for exam 2', 'Pay electric bill', 'Back up photos', 'Read 10 pages'] | Actual: {list_manager.get_items()}")

    format_header("Testing undo until empty list")
    list_manager.undo()
    print(f"Called Undo")
    print(f"Lenght of list manager | Expected: 3 | Actual: {list_manager.get_count()}")
    print(f"Items in list manager | Expected: ['Study for exam 2', 'Pay electric bill', 'Back up photos'] | Actual: {list_manager.get_items()}")
    print()
    list_manager.undo()
    print(f"Called Undo")
    print(f"Lenght of list manager | Expected: 2 | Actual: {list_manager.get_count()}")
    print(f"Items in list manager | Expected: ['Study for exam 2', 'Pay electric bill'] | Actual: {list_manager.get_items()}")
    print()
    list_manager.undo()
    print(f"Called Undo")
    print(f"Is list manager empty? | Expected: False | Actual: {list_manager.is_empty()}")
    print(f"Lenght of list manager | Expected: 1 | Actual: {list_manager.get_count()}")
    print(f"Items in list manager | Expected: ['Study for exam 2'] | Actual: {list_manager.get_items()}")
    print()
    list_manager.undo()
    print(f"Called Undo")
    print(f"Is list manager empty? | Expected: True | Actual: {list_manager.is_empty()}")
    print(f"Lenght of list manager | Expected: 0 | Actual: {list_manager.get_count()}")
    print(f"Items in list manager | Expected: [] | Actual: {list_manager.get_items()}")

    format_header("Testing clear")
    clear_manager = ListManager()
    clear_manager.add("Study for exam", 0)
    clear_manager.add("Pay bills", 1)
    clear_manager.add("Buy groceries", 2)

    print(f"Items before clear | Expected: ['Study for exam', 'Pay bills', 'Buy groceries'] | Actual: {clear_manager.get_items()}")
    print()
    print(f"Called Clear | Expected: True | Actual: {clear_manager.clear()}")
    print(f"Is list manager empty? | Expected: True | Actual: {clear_manager.is_empty()}")
    print(f"Length of list manager | Expected: 0 | Actual: {clear_manager.get_count()}")
    print(f"Items in list manager | Expected: [] | Actual: {clear_manager.get_items()}")

    format_header("Testing undo clear")
    print(f"Called Undo | Expected: True | Actual: {clear_manager.undo()}")
    print(f"Is list manager empty? | Expected: False | Actual: {clear_manager.is_empty()}")
    print(f"Length of list manager | Expected: 3 | Actual: {clear_manager.get_count()}")
    print(f"Items in list manager | Expected: ['Study for exam', 'Pay bills', 'Buy groceries'] | Actual: {clear_manager.get_items()}")

    format_header("Testing clear on empty list")
    empty_manager = ListManager()
    print(f"Is list manager empty? | Expected: True | Actual: {empty_manager.is_empty()}")
    print(f"Called Clear | Expected: False | Actual: {empty_manager.clear()}")
    print(f"Length of list manager | Expected: 0 | Actual: {empty_manager.get_count()}")
    print(f"Items in list manager | Expected: [] | Actual: {empty_manager.get_items()}")
    print(f"Called Undo | Expected: False | Actual: {empty_manager.undo()}")

    format_header("Testing undo after clear and add")
    clear_manager.clear()
    clear_manager.add("New task", 0)
    print(f"Items in list manager | Expected: ['New task'] | Actual: {clear_manager.get_items()}")
    print()
    clear_manager.undo()
    print("Called Undo")
    print(f"Items in list manager | Expected: [] | Actual: {clear_manager.get_items()}")
    print()
    clear_manager.undo()
    print("Called Undo")
    print(f"Items in list manager | Expected: ['Study for exam', 'Pay bills', 'Buy groceries'] | Actual: {clear_manager.get_items()}")


if __name__ == "__main__":
    main()
