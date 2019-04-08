class Hashtable():
    def __init__(self, n):
        self.hashtable = [[] for i in range(n)]

    def hashfunc(self, key):    
        return hash(key) % len(self.hashtable)

    def insert(self, key):
        self.hashtable[self.hashfunc(key)].append(key)

    def find(self, key):
        return self.hashfunc(key)

    def haskey(self, key):
        return key in self.hashtable[self.hashfunc(key)]