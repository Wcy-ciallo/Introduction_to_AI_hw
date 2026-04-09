class PriorityQueue:
    def __init__(self):
        self.items = []

    def push(self, priority, item):
        self.items.append((priority, item))

    def pop(self):
        if self.is_empty():
            return None
        
        min_index = 0
        for i in range(1, len(self.items)):
            if self.items[i][0] < self.items[min_index][0]:
                min_index = i
        
        return self.items.pop(min_index)
    def is_empty(self):
        return len(self.items) == 0