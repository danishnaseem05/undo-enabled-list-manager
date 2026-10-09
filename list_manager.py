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

    #private methods for pushing to undo stack
    def _insert_task(self, task, index):
        return self.linked_list.insert_at(index, task)

    def _remove_task(self, index):
        task = self.linked_list.get_at(index)
        self.linked_list.delete_at(index)
        return task

    #public methods
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
        pass

    def edit(self):
        pass

    def undo(self):
        if self.stack.is_empty_stack():
            return False

        undo_func = self.stack.get_top()
        self.stack.pop()
        undo_func()
        return True

    def get_items(self):
        pass
