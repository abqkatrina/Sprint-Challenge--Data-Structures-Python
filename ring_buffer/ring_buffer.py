# class Element:
#     def __init__(self, value):
#         self.value = value
#         self.next = next
#         self.prev = None

#     def delete(self):
#         if self.prev:
#             self.prev.next = self.next
#         if self.next:
#             self.next.prev = self.prev


# class DLL:
#     def __init__(self, elem=None):
#         self.head = elem
#         self.tail = elem
#         self.length = 1 if elem is not None else 0

#     def __len__(self):
#         return self.length

# #add to 0 pos (FIRST IN)
#     def addfirst(self, value):
#         #make a new element
#         new_el = Element(value)
#         #add element to empty list
#         if self.head is None:
#             self.head = new_el
#             self.tail = new_el
#             return
#         #add to front with old head next
#         new_el.next = self.head
#         #make old tail regular elem
#         self.head.prev = new_el
#         #define new head
#         self.head = new_el

# #add to end (LAST IN)
#     def addlast(self, value):
#         #make new element
#         new_el = Element(value)
#         #add element to empty list
#         if self.head is None:
#             self.head = new_el
#             self.tail = new_el
#             return
#         #add to end, move up old tail
#         new_el.prev = self.tail
#         #make old tail a regular element
#         self.tail.next = new_el
#         #define new tail
#         self.tail = new_el

# #FIRST OUT
#     def popfirst(self):
#         self.delete(self.head)

# #LAST OUT
#     def poplast(self):
#         self.delete(self.tail)

# #mave to 0 pos
#     def move_to_first(self, elem):
#         #if already head
#         if elem is self.head:
#             return
#         #make element new head
#         self.addfirst(elem)
#         #erase element from previous pos
#         self.delete(elem)

# #move to end
#     def move_to_last(self, elem):
#         #if already tail
#         if elem is self.tail:
#             return
#         #make element new tail
#         self.addlast(elem)
#         #erase element from prev pos
#         self.delete(elem)

# #delete node (from middle)
#     def delete(self, elem):
#         #minus 1 from length
#         self.length -= 1
#         #if only element in list
#         if self.head is self.tail:
#             self.head = None
#             self.tail = None
#         #if element is head
#         elif elem is self.head:
#             self.head = elem.next
#             elem.delete()
#         #if element is tail
#         elif elem is self.tail:
#             self.tail = elem.prev
#             elem.delete()
#         #if regular element
#         else:
#             elem.delete()


# class RingBuffer:
#     def __init__(self, capacity):
#         # A ring buffer is a non-growable buffer with a FIXED SIZE. 
#         self.capacity = capacity
#         self.storage = DLL()
#         self.length = 0

# When the ring buffer is full and a new element is inserted, the OLDEST element in the ring buffer is OVERWRITTEN WITH the NEWEST element.
# The `append` method adds the given element to the buffer. 
    # def append(self, item):
    #     new_el = Element(item)
    #     self.length +=1
        
    #     if self.head is None:
    #         self.head = new_el
    #     self.rear.next = new_el
    #     self.rear = new_el

    #     return new_el

# The `get` method returns all of the elements in the buffer in a list in their given order. It should not return any `None` values in the list even if they are present in the ring buffer.
    # def get(self):

    #     cur_el = self.capacity[0]
    #     return cur_el

class Item:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
 

class BufferQueue:
    def __init__(self, capacity=0):
        self.queue = []
        self.capacity = capacity
        self.length = 0
        self.front = None
        self.rear = None
    
    def append(self, item):
        #make a new item
        new_item = Item(item)
        #add to length
        self.length +=1

        #if queue is empty, make a front/rear item
        if self.front is None:
            self.front = new_item
            self.rear = new_item
            return

        #if queue not full, add to rear
        # +d = abc -> abcd
        if self.length < self.capacity:
            self.rear = new_item
            
        #if at capacity, add new to front
        # abcde -> fbcde AND abcdefghi -> fghie
        #if add one to full, replace front with new
        if self.length == self.capacity:
            self.front = new_item
        #if add many to full, move front to rear?

        

    



    def get(self):
        i = self.front
        while i:
            self.queue.append(i.value)
            i = i.next
        return self.queue

            
            



# For example:
# <!-- FIFO append something new to last, first in line popped -->
# <!-- Make RingBuffer class with append and get methods -->
# <!-- get method returns all but 'None' -->
# stack, queue, sll, or dll?
#stack is LIFO X
#queue size fixed, contiguous storage, index based
#sll size not fixed, scattered storage, reference based
#dll size not fixed, scattered storage, reference based