# singlely linked list

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next
        return new_next

class LinkedList:
    def __init__(self):
        # the first Node in the LinkedList
        self.head = None
        # the last Node in the LinkedList
        self.tail = None

    def add_to_tail(self, value):
        # create a new node if none exist
        new_node = Node(value, None)
        # check to see if the list is empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # create new node with first value
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None
        # save the Node's value
        value = self.head.get_value()

        # if there's only one Node in the linked list
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            # update the self.head to refer to the new node
            self.head = self.head.get_next_node()
        return value
    
    def contains(self, value):
        # an empty linked list can't contain what we're looking for 
        if not self.head:
            return False

        # get a reference to the first Node in the linked list 
        # we update what this Node points to as we traverse the linked list
        current = self.head

        # traverse the linked list so long as `current` is referring
        # to a Node
        while current is not None:
            # check if the Node that `current` is pointing at is holding
            # the data we're looking for
            if current.get_value() == value:
                return True
            # update our `current` pointer to point to the next Node in the linked list
            current = current.get_next_node()

        # we checked the whole linked list and didn't find the data
        return False

    def get_max(self):
        if self.head is None:
            return None
        current_max_val = self.head.get_value()

        current = self.head.get_next_node()

        while current is not None:
            if current.get_value() > current_max_val:
                current_max_val = current.get_value()

            current = current.get_next_node()

        return current_max_val

    def remove_tail(self):
        if self.tail is None:
            return None
        #save the new tail
        value = self.tail.get_value()
        if self.head is self.tail:
            # set both to none
            self.head = None
            self.tail = None
        else:
            # update self.tail to point to the Node before the tail
            #because we can't move backwards from any one Node so we start at the beginning
            current = self.head

            # traverse the node
            while current.get_next_node() != self.tail:
                current = current.get_next_node()

                #current is now pointing at the Node right before tail
            self.tail = current
            return value
