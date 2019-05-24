class Node:
    """Class for Node representation"""
    def __init__(self, value, left=None, right=None):
        """
        Initialization of Node
        """
        self.left = left
        self.right = right
        self.value = value

    def get_value(self):
        return self.value