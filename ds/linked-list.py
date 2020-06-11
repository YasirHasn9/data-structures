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


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tai(self, value):
        new_node = Node(value, None)
        # each node has a head and tail , no we need add to the tail
        # but what if we have an empty tail ?
        # how would we know if ll is empty ?
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node  # -> new_node = Node("value" , None)

    def remove_head(self):
        if not self.head:
            return None
           # if head has no next , then we have only a single element in the list
        if not self.head.get_next():
            # get referenced to the head
            head = self.head
            # delete the head
            self.head = None
            # make sure that the tail does not point to anything
            self.tail = None

            # return new value
            return head.get_value()

        # other wise we have more than one element
        value = self.head.get_value()
        # set the head reference to the current head's next node in the list
        self.head = self.head.get_next()
        return value

    def contains(self, value):
        if not self.head:
            return False

        # get the node that we are currentely at
        current = self.head
        while current:
            if current == value:
                return True
        # update our current to current node
            current = current.get_next()

        return False
