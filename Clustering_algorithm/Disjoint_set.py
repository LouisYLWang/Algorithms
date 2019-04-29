class Disjoint_set():
    def __init__(self):
        self.head = None
        self.tail = None

    def add_element(self, element):
        if self.head != None:
            self.tail.next = element
        else:
            self.head = element
        self.tail = element
        element.set = self

    def __str__(self):
        return str([self.head.label, self.tail.label])
    
    def get_elements(self):
        elements_ls = [self.head.label]
        ele = self.head
        while ele.next:
            elements_ls.append(ele.next.label)
        return elements_ls


class Element():
    def __init__ (self, label):
        self.set = None
        self.next = None
        self.label = label

    def update_set(self, set):
        self.set = set

    def find_set(self):
        print(self.set.get_elements)
        return self.set

    def __str__(self):
        return str(self.label)


vertices = [Element(i) for i in range(10)]
set1 = Disjoint_set()
set1.add_element(vertices[0])
set1.add_element(vertices[8])
set1.add_element(vertices[3])
print(set1)
#print(vertices[0].find_set())
print(vertices[0].next)
#set1.get_elements()