# con of arrays - adding new contiguous chunk of memory and moving all the element
# is expensive, especially when compared to adding an element when there is already space
# also can't leave array where array is not contiguous with the exception of the end
# so using a .pop() method destroys the array

# linked lists have to start from the head and don't have a reference/index spot in the list
# linked lists are not contiguous in their memory representation

# will typically see Doubly linked lists in the wild

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev_node
        self.next = next_node
    
    def new_node():
        pass