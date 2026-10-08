"""
Author:
Date:

Purpose:

Input:

Output:
"""
from uuid import uuid4

class Task():
    def __init__(self, data):
        self.id = str(uuid4())
        self.data = data
