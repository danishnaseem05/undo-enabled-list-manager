"""
Author:
Date:

Purpose:

Input:

Output:
"""

from functools import partial

from my_linked_list import MyLinkedList
from my_stack import MyStack
from task import Task


class ListManager:
    def __init__(self, linked_list=None, stack=None):
        self.linked_list = linked_list if linked_list is not None else MyLinkedList()
        self.stack = stack if stack is not None else MyStack()

    # Private methods mutate the list without recording undo operations.
    def _insert_task(self, task, index):
        return self.linked_list.insert_at(index, task)

    def _remove_task(self, index):
        task = self.linked_list.get_at(index)
        self.linked_list.delete_at(index)
        return task

    def _move_task(self, from_pos, to_pos):
        task = self._remove_task(from_pos)
        self._insert_task(task, to_pos)

    def _edit_task(self, task, data):
        task.set_data(data)

    # Public methods mutate the list and record their inverse operations.
    def add(self, item, index):
        if index < 0 or index > self.linked_list.get_count():
            return False

        task = Task(item)
        self._insert_task(task, index)
        self.stack.push(partial(self._remove_task, index))
        return True

    def remove(self, index):
        if index < 0 or index >= self.linked_list.get_count():
            return False

        task = self._remove_task(index)
        self.stack.push(partial(self._insert_task, task, index))
        return True

    def move(self, from_pos, to_pos):
        count = self.linked_list.get_count()
        if not (0 <= from_pos < count and 0 <= to_pos < count):
            return False

        if from_pos == to_pos:
            return True

        self._move_task(from_pos, to_pos)
        self.stack.push(partial(self._move_task, to_pos, from_pos))
        return True
    
    def edit(self, index, new_data):
        if index < 0 or index >= self.linked_list.get_count():
            return False

        task = self.linked_list.get_at(index)
        old_data = task.get_data()

        self._edit_task(task, new_data)
        self.stack.push(partial(self._edit_task, task, old_data))
        return True

    def undo(self):
        if self.stack.is_empty_stack():
            return False

        undo_func = self.stack.get_top()
        self.stack.pop()
        undo_func()
        return True

    def get_items(self) -> list:
        tasks: list = self.linked_list.to_array()

        task_data = []
        for task in tasks:
            task_data.append(task.get_data())

        return task_data

    def is_empty(self):
        return self.linked_list.is_empty()

    def get_count(self):
        return self.linked_list.get_count()
