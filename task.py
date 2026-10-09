"""
Author:
Date:

Purpose:

Input:

Output:
"""
from uuid import uuid4


class Task:
    def __init__(self, data):
        self.id = str(uuid4())
        self.data = data

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data
