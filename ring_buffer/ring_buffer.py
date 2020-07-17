class Element:
    def __init__(self, value):
        self.value = value
        self.next = next
        self.prev = None

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DLL:
    def __init__(self, elem=None):
        self.head = elem
        self.tail = elem
        self.length = 1 if elem is not None else 0

    def __len__(self):
        return self.length

#add to 0 pos (FIRST IN)
    def addfirst(self, value):
        #make a new element
        new_el = Element(value)
        #add element to empty list
        if self.head is None:
            self.head = new_el
            self.tail = new_el
            return
        #add to front with old head next
        new_el.next = self.head
        #make old tail regular elem
        self.head.prev = new_el
        #define new head
        self.head = new_el


#add to end (LAST IN)
    def addlast(self, value):
        #make new element
        new_el = Element(value)
        #add element to empty list
        if self.head is None:
            self.head = new_el
            self.tail = new_el
            return
        #add to end, move up old tail
        new_el.prev = self.tail
        #make old tail a regular element
        self.tail.next = new_el
        #define new tail
        self.tail = new_el

#FIRST OUT
    def popfirst(self):
        self.delete(self.head)

#LAST OUT
    def poplast(self):
        self.delete(self.tail)

#mave to 0 pos
    def move_to_first(self, elem):
        pass

#move to end
    def move_to_last(self, elem):
        pass

#delete node (from middle)
    def delete(self, elem):
        #minus 1 from length
        self.length -= 1
        #if only element in list
        if self.head is self.tail:
            self.head = None
            self.tail = None
        #if element is head
        elif elem is self.head:
            self.head = elem.next
            elem.delete()
        #if element is tail
        elif elem is self.tail:
            self.tail = elem.prev
            elem.delete()
        #if regular element
        else:
            elem.delete()




class RingBuffer:
    def __init__(self, capacity):
        # A ring buffer is a non-growable buffer with a FIXED SIZE. 
        self.capacity = capacity
        self.storage = DLL()

# When the ring buffer is full and a new element is inserted, the OLDEST element in the ring buffer is OVERWRITTEN WITH the NEWEST element.
# The `append` method adds the given element to the buffer. 
    def append(self, item):
        new_el = Element(item)
        return new_el

# The `get` method returns all of the elements in the buffer in a list in their given order. It should not return any `None` values in the list even if they are present in the ring buffer.
    def get(self):

        cur_el = self.capacity[0]
        return cur_el



# For example:
# <!-- FIFO append something new to last, first in line popped -->
# <!-- Make RingBuffer class with append and get methods -->
# <!-- get method returns all but 'None' -->