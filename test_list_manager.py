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

    # Added tests for clear and undo clear.
    format_header("Testing clear on a populated list")
    clear_manager = ListManager()
    original_tasks = ["Homework", "Shopping", "Exercise"]
    for index, task in enumerate(original_tasks):
        assert clear_manager.add(task, index) is True

    assert clear_manager.clear() is True
    assert clear_manager.is_empty() is True
    assert clear_manager.get_count() == 0
    assert clear_manager.get_items() == []
    print("PASS: clear() removes all tasks from a populated list")

    format_header("Testing undo clear")
    assert clear_manager.undo() is True
    assert clear_manager.get_items() == original_tasks
    assert clear_manager.get_count() == len(original_tasks)
    print("PASS: undo() restores all tasks in their original order")

    format_header("Testing clear on an empty list")
    empty_manager = ListManager()
    assert empty_manager.clear() is False
    assert empty_manager.get_items() == []
    assert empty_manager.undo() is False
    print("PASS: clear() on an empty list does not create an undo action")

    format_header("Testing undo order after clear and add")
    history_manager = ListManager()
    assert history_manager.add("First", 0) is True
    assert history_manager.add("Second", 1) is True
    assert history_manager.clear() is True
    assert history_manager.add("New", 0) is True
    assert history_manager.undo() is True
    assert history_manager.get_items() == []
    assert history_manager.undo() is True
    assert history_manager.get_items() == ["First", "Second"]
    print("PASS: undo() first reverses add, then restores the cleared list")

    format_header("All clear and undo clear tests passed")


if __name__ == "__main__":
    main()
