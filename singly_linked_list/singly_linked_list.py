class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        # returns the node's data
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    '''
    Adds `data` to the end or the begining of the LinkedList 
   is O(1)  
    '''

    def add_to_tail(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node)
            self.tail = node

    def remove_tail(self):
        if self.head is None:
            return None
        # save the tail Node's data
        node_value = self.tail.get_value()
      
    #   if there is only one node in the list
        if self.head == self.tail:
            # set both to be None
            self.head = None
            self.tail = None
        else:

     
            current = self.head


            # before the tail Node
            while current.get_next() != self.tail:
                current = current.get_next()

       
            self.tail = current

        return node_value


    def remove_head(self):
        if self.head is None:
            return None
        data = self.head.get_value()
    
        # there's only one Node in the linked list
        if self.head is self.tail:
            # set both to be None
            self.head = None
            self.tail = None
        else:

            self.head = self.head.get_next()

        return data


 

    def contains(self, data):

        if not self.head:
            return False

  
        current = self.head

      
        while current is not None:
           
            if current.get_value() == data:
                return True
            
            current = current.get_next()

       
        return False

  
    def get_max(self):
        if self.head is None:
            return None

        max = self.head.get_value()

        current = self.head.get_next()

        while current is not None:
            if current.get_value() > max:
                max = current.get_value()

            current = current.get_next()

        return max
