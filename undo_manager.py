"""
Author:
Date:

Purpose:

Input:

Output:
"""

from task import Task

class UndoManager():    
    def undo_add(self):
        pass

    def undo_remove(self):
        pass

    def undo_move(self, list, from_pos: int, to_pos: int, item: Task):
        def undo():
            list.delete_at(from_pos)
            list.insert_at(to_pos, item)

        return undo

    def undo_edit(self):
        pass
