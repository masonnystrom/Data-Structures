"""
Measuring efficiency
1)timer: approach doesn't give consistency, will vary by algorithm and computer
2)count operations: lacks standardization
Mathematical operations, comparisons, assignments, and accessing objs in memory are diff operations
runtime is not predictable w/ small inputs

Runetime complexity
    standardized way of describing the efficiency of code/algorithms

best and worse case scenarios

Big Oh notation
O()

# it always takes the same amount of time to find an element at a specific index

"""
list = [1,2,3,4,5]
def add_five(list):
    for x in list:
        pass

list = [3,6,9,12]
# elem 3 takes 1 second
# elem 9 takes 3 seconds
# linear runtime
def search_for_elemt(L, e):
    for i in L:
        if i == e:
            return True
    return False

# contiguous vs linked data structures
# contiguous: single slabs of memory( arrays, matrices, heaps, and hash tables)
# linked; multipled distinct chunkcs of memory bound together by pointers, and include linkedlist and trees

for command in commands:
    pass

# congiuous data

class Node:
    def __init__(self, value=None, next_node=None):
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
    def __ini__(self):
        self.head = None
        self.tail = None
    def add_to_tail(self, value):
        # 0. create new node
        new_node = Node(value, None)
        # 1. check to see if the list is empty
        if not self.head:
            # if the list is empty, set both head and tail to node
            self.head = new_node
            self.tail = new_node
        # 2. create a new node with value arg
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
        # 3. it depends
    def remove_head(self):
        if not self.head:
            return None
        # if head has no next,
        if not self.head.get_next_node:
            head = self.head
            self.head = None
            # set tail reference to None 
            self.tail = None
            return head.get_value()
        value = self.head.get_value()





class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    def insert(self, data):
        self.head = Node(data, self.head)
        self.length += 1
    def remove_at_index(self, idx):
        dummy = Node(None, self.head)
        prev, curr = dummy, dummy.next
        check_idx = 0
        while curr:
            print(idx, check_idx)
            if idx == check_idx:
                prev.next = curr.next
                curr.next = None
            check_idx += 1
            prev, curr = curr, curr.next
    def iterate(self):
        node = self.head
        while(node):
            print(node.data)
            node = node.next
    def search(self, data):
        idx = 0
        node = self.head
        while node:
            if node.data == data: return idx
            node = node.next
            idx += 1
        return -1