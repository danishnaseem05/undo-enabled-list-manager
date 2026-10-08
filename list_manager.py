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
from undo_manager import UndoManager
from task import Task

class ListManager():
    def __init__(self, linked_list=None, stack=None):
        if linked_list is None:
            self.linked_list = MyLinkedList
        else:
            self.linked_list = linked_list

        if stack is None:
            self.stack = MyStack
        else:
            self.stack = stack

        self.undo_manager = UndoManager()

    def add(self, item):
        pass

    def remove(self, index):
        pass

    def move(self, from_pos: int, to_pos: int) -> None:
        curr_task: Task = self.linked_list.get_at(from_pos)
        self.linked_list.delete_at(from_pos)
        self.linked_list.insert_at(to_pos, curr_task)
        self.stack.push(
            partial(
                self.undo_manager.undo_move,
                list=self.linked_list,
                from_pos=to_pos,
                to_pos=from_pos,
                item=curr_task    
            )
        )

    def edit(self):
        pass

    def undo(self):
        pass

    def get_items(self) -> list:
        tasks: list = self.linked_list.to_array()

        task_data = []
        for task in tasks:
            task_data.append(task.get_data())

        return task_data
