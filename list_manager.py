"""
Author:
Date:

Purpose:

Input:

Output:
"""

from my_linked_list import MyLinkedList
from my_stack import MyStack

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

    def add(self, item):
        pass

    def remove(self, index):
        pass

    def move(self, from_pos, to_pos):
        pass

    def edit(self):
        pass

    def undo(self):
        pass

    def get_items(self):
        pass
