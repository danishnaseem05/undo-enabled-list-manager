"""
Authors: Daniel Adayev, Kevin Cang, Danish Naseem, Abdullah Rizwan
Date: October 11, 2026

Purpose: Represent one task with a unique identifier and editable data.
Input: The data used to describe a task.
Output: A Task instance with a UUID and stored data.
"""
from uuid import uuid4


class Task:
    """Store a task's unique identifier and editable data."""

    def __init__(self, data):
        self.id = str(uuid4())
        self.data = data

    def get_data(self):
        """Return the task's data."""

        return self.data

    def set_data(self, data):
        """Replace the task's data."""

        self.data = data
