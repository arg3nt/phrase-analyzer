class Lexeme:
    def __init__(self, val, prune_threshold=2):
        self.prev = {}
        self.next = {}
        self.value = val
        self.threshold = prune_threshold
    
    def __str__(self):
        return self.value

    def addNext(self, word):
        if not self.next.get(word):
            self.next[word] = 1
        else:
            self.next[word] += 1
    
    def addPrev(self, word):
        if not self.prev.get(word):
            self.prev[word] = 1
        else:
            self.prev[word] += 1
    
    def prune(self):
        delete_keys = []
        for k in self.next.keys():
            if self.next[k] < self.threshold:
                delete_keys.append(k)
        
        for k in delete_keys:
            del self.next[k]
        delete_keys.clear()
        
        for k in self.prev.keys():
            if self.prev[k] < self.threshold:
                delete_keys.append(k)
        
        for k in delete_keys:
            del self.prev[k]
