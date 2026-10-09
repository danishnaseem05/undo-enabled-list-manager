"""
Author:
Date:

Purpose: This program implements a singly linked list using individual node objects linked together. Each node object contain a data element which contains the actual value to be stored, and a next element, which is a pointer referencing to the next node in the list. The methods implemented enable the capability to be able to insert and delete items to and from the the list.

Input: It can be initialized in two ways different ways:
- It can be initialized without any arguments.
- By calling the `from_array` method which initializes the linked list with the items contained in the specified python list.

Output: It outputs a singly linked list, which is either one of the two during the instantiation:
- It can be a linked list with no items, it's head and tail being None, and lenght of zero.
- It can be a linked list consisting of node objects containing the values of a python list input by the user, with its head referencing the node object containing the first value, and tail referencing the node object containing the last value. Also the its length being equal to the number of elements in the input python list.
"""


class _Node:
    """
    Precondition: takes in the following arguments:
    - data (int): the value to be stored.
    - next (None | _Node): defaulted to None, but can be another _Node object.

    Postcondition: outputs a singly linked list node having data and a reference to the next node (or None if this is the only or last node).
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class MyLinkedList:
    """
    Precondition: no inputs being passed in.

    Postcondition: returns an instance of the MyLinkedList with first and last referencing to None, and a count of 0. Thus this represents an empty singly linked list.
    """
    def __init__(self):
        self._first = None
        self._last = None
        self._count = 0

    @classmethod
    def from_array(cls, items):
        """
        Precondition: takes in a items, which is a python list (or other iterable) contaning values of type int to initialize this linked list with.

        Postcondition: returns a new instance of the MyLinkedList containing a node for each value in items, in the same order, with the help of the `add_last` method.
        """
        my_linked_list = cls()
        for i in range(len(items)):
            my_linked_list.add_last(items[i])
        return my_linked_list

    def copy_list(self, other):
        """
        Precondition: takes in other, which is an instance of the MyLinkedList. other may be the same object as self.

        Postcondition: returns None. if self is other, does nothing, otherwise, with the help of the `add_last` method, adds data of each node in other to self, without copying the reference to the node itself, thus self becomes a deep copy of other's contents.
        """
        if self is other:
            return

        current = other.get_at(0)
        while current != None:
            self.add_last(current.data)
            current = current.next

    def get_count(self):
        """
        Precondition: no inputs being passed in.

        Postcondition: returns int, which is the number of items currently stored in this list.
        """
        return self._count

    def is_empty(self):
        """
        Precondition: no inputs being passed in.

        Postconditions: returns boolean, True if this list has no nodes, otherwise False. This check is performed by checking whether `_first` is None or not.
        """
        return self._first is None

    def __str__(self):
        """
        Precondition: no inputs being passed in.

        Postcondition: returns str. If the list contains no nodes, "EMPTY LIST" is returned, otherwise it returns each node's value separated by " -> ", with no trailing arrow after the last element.
        """
        result = ""
        current = self._first
        while current != None:
            result += str(current.data)
            if current.next != None:
                result += " -> "
            current = current.next

        return result if result else "EMPTY LIST"

    def to_array(self):
        """
        Precondition: no inputs being passed in.

        Postcondition: return list. If the MyLinkedList contains no nodes, empty python list is returned, otherwise it returns python list with each node's value
        """
        result = []
        current = self._first
        while current != None:
            result.append(current.data)
            current = current.next

        return result

    def get_first(self):
        """
        Precondition: no inputs being passed in.

        Postcondition: returns the value stored in the first node.
        """
        return self._first.data

    def get_last(self):
        """
        Precondition: no inputs being passed in.

        Postcondition: returns the value stored in the last node.
        """
        return self._last.data

    def get_at(self, index):
        """
        Precondition: index of type int is passed in. It is assumed the index is already within the constraints (0 <= index < self.get_count()).

        Postcondition: returns the node object's `data` stored at that given index. The returned object is not a copy, rather the actual object that the caller can mutate the attributes of in place.
        """
        current = self._first
        counter = 0
        while current != None:
            if counter == index:
                return current.data
            counter += 1
            current = current.next

    def search(self, item):
        """
        Precondition: takes in item of type int, which is the value to search for in this linked list.

        Postcondition: returns boolean. True if the item is found in the list, False otherwise. Calls `index_of` method as not to duplicate the same search logic.
        """
        return self.index_of(item) != -1

    def _handle_empty_insert(self, item):
        """
        Precondition: takes in item of type int, which is the value to be added to this linked list (if empty). This is a helper method called across various insert methods as not to duplicate the logic.

        Postcondition: returns boolean. True, if this linked list is empty and the item was added as the first node object containing the item, False otherwise. When adding the item, it creates a new node object containing the value of the item, then updates both first and last to point to this new node, and count is incremented by 1.
        """
        if self._first == None:
            node = _Node(item)
            self._first = node
            self._last = node
            self._count += 1
            return True
        return False

    def add_first(self, item):
        """
        Precondition: takes in item of type int, which is the value to be added to the start of this linked list.

        Postcondition: returns None. It calls `_handle_empty_insert` helper method to handle the empty list insert case. If the list is not empty, it creates a new node object containing the value of item, and adds in that node object to the start of the list. The first is updated to this node, and count is incremented by 1.
        """
        if self._handle_empty_insert(item):
            return

        node = _Node(item)
        node.next = self._first
        self._first = node
        self._count += 1

    def add_last(self, item):
        """
        Precondition: takes in item of type int, which is the value to be added to the end of this linked list.

        Postcondition: returns None. It calls `_handle_empty_insert` helper method to handle the empty list insert case. If the list is not empty, it creates a new node object containing the value of item, and adds in that node object to the end of the list. The last is updated to this node, and count is incremented by 1.
        """
        if self._handle_empty_insert(item):
            return

        node = _Node(item)
        self._last.next = node
        self._last = node
        self._count += 1

    def insert_at(self, index, item):
        """
        Precondition: takes in index of type int and item of type int. item is the value to be inserted at index.

        Postcondition: returns bool. True, if the item was successfully inserted at index, otherwise the list if left unchanged and False in returned. It first checks to see whether index is within the constraints (0 <= index <= count), if not, returns False. During insertion, it calls `_handle_empty_insert` helper method to handle the empty list insert case. If the list if not empty, then it creates a new node object containing the value of item, and adds in that node object at the index position, and increments the count by 1.

        Two additional edge cases are accounted for if the list is not empty:
        - The item needs to be after the last item, in which case, last is updated to this new node object.
        - The item need to be added at the start of the list, in which case, first is updated to this new node object.
        """

        if index >= 0 and index <= self._count:
            # Two edge cases:
            # 1. Handle empty list
            if self._handle_empty_insert(item):
                return True
            # 2. Item to be added is after the last item
            if index == self._count:
                node = _Node(item)
                self._last.next = node
                self._last = node
                self._count += 1
                return True

            counter = 0
            current = self._first
            previous = None

            while current != None:
                if counter == index:
                    node = _Node(item)

                    # Special case: add the item as first position
                    if previous == None:
                        node.next = self._first
                        self._first = node
                        self._count += 1
                        return True
                    # Add item somewhere in the middle
                    node.next = previous.next
                    previous.next = node
                    self._count += 1
                    return True

                previous = current
                current = current.next
                counter += 1

        return False

    def _remove_after(self, node):
        """
        Precondition: takes in node of type _Node, which is the node previous to the node to be removed from this linked list. This is a helper method called from the different delete methods as not to duplicate the deletion logic.

        Postcondition: returns None. Removes the node object after the given node, by cutting of the references to that node. And decrements the count by 1.

        Few edges cases are accounted for during the removal:
        - The given node is None, meaning the node to be removed is the first node, in which case the first is updated to first's next node. Also if the first's next node is None, that means the list only had one element, and last is also updated to None.
        - The given node's next.next is None, meaning the the node to be removed is the last item, in which case the last is updated to the given node.
        """

        # Sepcial case, remove the first item
        if node == None:
            successor = self._first.next
            # The list only has one item
            if successor == None:
                self._last = None
            else:
                self._first.next = successor.next

            self._first = successor
        else:
            successor = node.next.next
            node.next = successor
            # The item to be removed is the last item
            if successor == None:
                self._last = node

        self._count -= 1

    def delete_item(self, item):
        """
        Precondition: takes in item of type int. item is the value to be removed.

        Postcondition: returns None. Removes the first occurrence of item. If item is not found, the list is left unchanged. Traverses the linked list from the left, starting from the first as current, while keeping track of the previous node, which starts at None and is one step behind the current node. If the current node's data equals to the item, then the `_remove_after` helper method is called with the previous node, in order to remove the node after it, which is the current node.
        """
        current = self._first
        previous = None

        while current != None:
            if current.data == item:
                self._remove_after(previous)
                return

            previous = current
            current = current.next    

    def delete_at(self, index):
        """
        Precondition: takes in index of int, which is the postion in the linked list, at which is node is to be removed.

        Postcondition: returns bool. True if the node is successfully removed at the given index, otherwise the list is left unchanged and False is returned. It first checks to see whether the index is within the constraints (0 <= index < count), if not, returns False. Traverses the linked list from the left, starting from the first as current, while keeping track of the previous node, which starts at None and is one step behind the current node. An additional counter is there to check when it reaches the specified index. Once reached, it calls `_remove_after` helper method with the previous node, is order the remove the node after it, which is the current node.
        """
        if index >= 0 and index < self._count:
            counter = 0
            current = self._first
            previous = None

            while current != None:
                if counter == index:
                    self._remove_after(previous)
                    return True

                counter += 1
                previous = current
                current = current.next

        return False

    def index_of(self, item):
        """
        Precondition: takes in item of type int, which is the item to search for in this linked list.

        Postcondition: return int, which is either the index of the first occurrence of item in the list, if found, otherwise -1 is returned.
        """
        index = 0
        current = self._first

        while current != None:
            if current.data == item:
                return index 

            index += 1
            current = current.next

        return -1

    def __eq__(self, other):
        """
        Precondition: takes in other, which is of type any. It could be of type MyLinkedList, but can be of any other object type.

        Postcondition: returns bool or NotImplemented. If the type of other is anything other than MyLinkedList, then NotImplemented is returned, otherwise a boolean value is returned. In the case of boolean value, returns True only if other has the same length and the same values in the same order as self. Otherwise returns False.
        """
        if not isinstance(other, MyLinkedList):
            return NotImplemented

        if other.get_count() != self.get_count():
            return False

        current_self = self._first
        current_other = other.get_at(0)

        while current_self != None and current_other != None:
            if current_self.data != current_other.data:
                return False
            
            current_self = current_self.next
            current_other = current_other.next

        return True

    def __ne__(self, other):
        """
        Precondition: takes in other, which is of type any. It could be of type MyLinkedList, but can be of any other object type.

        Postcondition: returns bool or NotImplemented. If the type of other is anything other than MyLinkedList, then NotImplemented is returned, otherwise a boolean value is returned. In the case of boolean value, it returns the logical opposite of __eq__, which is, it returns False only if other has the same length and the same values in the same order as self. Otherwise returns True.
        """
        if not isinstance(other, MyLinkedList):
            return NotImplemented

        if other.get_count() != self.get_count():
            return True

        current_self = self._first
        current_other = other.get_at(0)

        while current_self != None and current_other != None:
            if current_self.data != current_other.data:
                return True

            current_self = current_self.next
            current_other = current_other.next

        return False

    def clear(self):
        """
        Precondition: no inputs being passed in.

        Postcondition: returns None. It clears the entire list, reseting it to an empty state by setting the first and last to None, and resets the count to 0.
        """
        self._first = None
        self._last = None
        self._count = 0
