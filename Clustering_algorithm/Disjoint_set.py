from collections import Iterator, Iterable

class Disjoint_set(Iterable):
    def __init__(self, element=None):
        self.head = element
        self.tail = element
        element.set = self


    def add_element(self, element):
        if self.head != None:
            self.tail.next = element
        else:
            self.head = element
        self.tail = element
        element.set = self

    def __str__(self):
        if not self.is_empty():
            return str([self.head.label, self.tail.label])
        else:
            return 'empty set'
    
    def get_elements(self):
        if not self.is_empty():
            elements_ls = [self.head.label]
            ele = self.head
            while ele.next:
                elements_ls.append(ele.next.label)
                ele = ele.next
            return elements_ls
        else:
            return []

    def get_len(self):

        if not self.is_empty():
            set_len = 1
            ele = self.head
            while ele.next:
                set_len+=1
                ele = ele.next
            return set_len
        else:
            return 0

    def is_empty(self):
        return self.head == None

    def __iter__(self):
        if not self.head:
            return
        ele = self.head
        yield ele
        while ele.next:
            ele = ele.next
            yield ele
    

class Element():
    def __init__ (self, label):
        self.set = None
        self.next = False
        self.label = label

    def show_set(self):
        return(self.set.get_elements())

    def __str__(self):
        return str(self.label)


def union(set1, set2):
    if set1.get_len() > set2.get_len():
        max_set = set1
        min_set = set2
    else:
        min_set = set1
        max_set = set2

    max_set.tail.next = min_set.head
    max_set.tail = min_set.tail

    cur = min_set.head
    cur.set = max_set
    while cur.next:
        cur = cur.next
        cur.set = max_set

    min_set.head = None
    min_set.tail = False
    return max_set

