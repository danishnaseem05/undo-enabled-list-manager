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

class ListManager():
    def __init__(self, linked_list=None, stack=None):
        if linked_list is None:
            self.linked_list = MyLinkedList()
        else:
            self.linked_list = linked_list

        if stack is None:
            self.stack = MyStack()
        else:
            self.stack = stack

    def add(self, item):
        pass

    def _undo_add(self):
        pass

    def remove(self, index):
        pass

    def _undo_remove(self):
        pass

    def _move_task(self, from_index: int, to_index: int) -> bool:
        curr_task: Task = self.linked_list.get_at(from_index)
        self.linked_list.delete_at(from_index)
        self.linked_list.insert_at(to_index, curr_task)
    
    def move(self, from_index: int, to_index: int) -> bool:
        self._move_task(from_index, to_index)
        self.stack.push(
            partial(
                self._move_task,
                from_index=to_index,
                to_index=from_index,  
            )
        )
        return True

    def edit(self):
        pass

    def _undo_edit(self):
        pass

    def undo(self):
        pass

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
