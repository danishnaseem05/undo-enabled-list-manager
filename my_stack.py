"""
Author:
Date:

Purpose: This program implements a linked-list based stack data structure. It follows the LIFO (Last-In-First-Out) behavior. The last item to be added to the stack, is the first item to be removed from the stack. This item is called as the TOP. Inside the low-level linked-list, we save each item to the front (TOP) of the list as that is O(1) and simiarly during popping we remove the element from the front (TOP) of list as that is also O(1).

Input: It takes in no arugment during initialization, and initializes its parent `MyLinkedList` class as an empty linked list to serve as its backend storage.

Output: It outputs an empty linked-list based stack, that has the ability to push, pop, peek.
"""

from my_linked_list import MyLinkedList


class MyStack(MyLinkedList):
    """
    Input: Takes in no input, but inherits from the pre-implemented `MyLinkedList` class, and extends upon linked list's functionality.
    
    Output: Creates an empty `MyStack` by calling `MyLinkedList`'s constructor to consturct an empty linked list, thus serving as the backend storage for this stack.
    """
    def __init__(self):
        super().__init__()

    def is_empty_stack(self):
        """
        Input: Takes in no input.

        Output: Returns `bool`. `True` if the stack has no elements, `False` otherwise. Calls `MyLinkedList`'s `is_empty` method.
        """
        return self.is_empty()

    def push(self, item):
        """
        Input: Takes in the `item` to add to the stack. `item` can be of type `Any`.

        Output: Returns `None`. Calls `MyLinkedList`'s `add_first` method to add `item` to the start of the linked list, thus adding to the TOP of the stack.
        """
        # If it were a queue, which follows FIFO (First-In-First-Out) behavior,
        # we would have added the item to the end of the list using
        # `MyLinkedList`'s `add_last` method.
        return self.add_first(item)

    def pop(self):
        """
        Input: Takes in no input.

        Output: Returns `None`. Calls `MyLinkedList`'s `delete_at` method with the index of `0`, to remove the TOP element from the stack. 
        """
        # Similarly, if it were a queue, which follows FIFO (First-In-First-Out) behavior,
        # we again would have removed the first element from the list at
        # index 0, this is because in the queue we are adding the element
        # at the end of the list. Thus it has to be removed from the other
        # end of the list, which in this case is the start of the list.
        self.delete_at(0)

    def get_top(self):
        """
        Input: Takes in no input.

        Output: Returns `Any`. Calls `MyLinkedList`'s `get_first` method, to return the value of the TOP element of the stack. It does not modify the stack.
        """
        # Similarly, if it were a queue, which follows FIFO (First-In-First-Out)
        # behavior, we again would have retrieved the element from the
        # start of the list, as this element, being inserted from the end
        # of the list, has been waiting for its turn longer than the other
        # elements.
        return self.get_first()

    def get_count(self):
        """
        Input: Takes in no input.

        Output: Returns `int`. Calls `MyLinkedList`'s `get_count` method to return the number of elements currently present in the stack. Makes use of the `super` as both child and parent class functions share the same name of `get_count`.
        """
        return super().get_count()

    def __str__(self):
        """
        Input: Takes in no input.

        Output: Returns `str`. `"EMPTY STACK"` if stack has no elements, otherwise returns a string containing the value of each element in the stack, one per line. To avoid referencing the parent's internal node objects, it makes use of a temporary `MyStack` that holds the elements during the traversal phase, where the elements are being popped from the original stack to be added to the result string. Once the traversal phase is done, the elements get restored back to the original stack, preserving their original ordering.
        """
        temp_stack = MyStack()
        result = ""

        while not self.is_empty_stack():
            item = self.get_top()
            temp_stack.push(item)

            result += str(item)
            if self.get_count() > 1:
                result += "\n"

            self.pop()

        while not temp_stack.is_empty_stack():
            self.push(temp_stack.get_top())
            temp_stack.pop()

        return result if result else "EMPTY STACK"
