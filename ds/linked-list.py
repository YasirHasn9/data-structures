'''
linked list is a data structure that store data each piece of data contains a node 
that have a head and tail where the points to the start and tail to the end
the node made of [value/next] box where store a value in random space in the memory 
and that value has a next that point to another node in somewhere that is relative
to the other 
prepands and appands are O(1) 
lookups are O(n)
'''


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, newNode):
        self.next_node = newNode


