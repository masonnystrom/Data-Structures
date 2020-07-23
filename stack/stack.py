from singly_linked_list import LinkedList

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
    Stacked works using First-in-first-out method whereas linked lisk stores
    data and address of other nodes
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         """Return length of stack"""
#         self.size = len(self.storage)
#         return self.size

#     def push(self, value):
#         """ add an element to the stack"""
#         self.storage.append(value)

#     def pop(self):
#         """ remove most recent element """
#         if len(self.storage) == 0:
#             return None
#         else:
#             return self.storage.pop(-1)


# class stack with linked list
class Stack():
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
          if self.__len__() == 0:
            return None
          else:
            removed_node_value = self.storage.tail.value
            self.storage.remove_tail()
            self.size -= 1

            return removed_node_value
