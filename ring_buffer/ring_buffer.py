class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev



class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        # create a list node
        new_node = ListNode(value)
        # Update length
        self.length += 1
        # if there is not a head or tail node
        if not self.head and not self.tail:
            # new node will be head and tail
            self.head = new_node
            self.tail = new_node
        # there is already a node
        else:
            # new nodes next is the current head
            new_node.next = self.head
            # current head will no longer be head so it will have a previous pointer to the new node
            self.head.prev = new_node
            # set new node as the head
            self.head = new_node

    def remove_from_head(self):
        # Capture value of node to remove
        value = self.head.value
        # Use ListNode delete method
        self.delete(self.head)
        # Return the value
        return value

    def add_to_tail(self, value):
        # create new node
        new_node = ListNode(value)
        # update length
        self.length += 1
        # if there is not a head or tail
        if not self.head and not self.tail:
            # new node will be head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # new node previous pointer becomes current tail
            new_node.prev = self.tail
            # current tail will no longer be the tail so it will now have a next pointer to the new node
            self.tail.next = new_node
            # set new node as the tail
            self.tail = new_node

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    def move_to_front(self, node):
        # If already the head
        if node is self.head:
            return
        self.add_to_head(node.value)
        self.delete(node)

    def move_to_end(self, node):
        # If already the tail
        if node is self.tail:
            return
        self.add_to_tail(node.value)
        self.delete(node)

    def delete(self, node):
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = node.next
            node.delete()
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()


class RingBuffer(DoublyLinkedList):
    def __init__(self, capacity):
        self.queue =[]
        self.capacity = capacity
        # move values, need temp
        self.current_node = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # storage is less than capacity
        if len(self.storage) < self.capacity:
            # Easy, just add item to tail
            # Head [a] Tail
            # Head [a, b] Tail
            # Head [a, b, c] Tail
            self.storage.add_to_tail(item)
        # storage is at capacity
        else:
            # If current_node is None, it's the first time trying to add to a full capacity
            if self.current_node == None:
                # The first time we add to our list on full capacity, we will be replacing the head's VALUE
                self.storage.head.value = item
                # Set the current_node to the head's next node
                self.current_node = self.storage.head.next
            # The current_node is already assigned
            else:
                # Now we can just replace the current_node's value with the new item
                self.current_node.value = item
                # Just like before we now set the current_node
                # but this time with the current_node's next node'
                self.current_node = self.current_node.next

    

# The `get` method returns all of the elements in the buffer in a list in their given order. It should not return any `None` values in the list even if they are present in the ring buffer.


    def get(self):
        current_node = self.storage.head
        while current_node:
            self.queue.append(current_node.value)
            current_node = current_node.next
        return self.queue

            
            



# For example:
# <!-- FIFO append something new to last, first in line popped -->
# <!-- Make RingBuffer class with append and get methods -->
# <!-- get method returns all but 'None' -->
# stack, queue, sll, or dll?
#stack is LIFO X
#queue size fixed, contiguous storage, index based
#sll one direction -- dll is more flexible
#dll size not fixed, scattered storage, reference based


