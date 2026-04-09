class Graph:
    def __init__(self):
        self.adj = {}
    
    def add_node(self, node):
        if node not in self.adj:
            self.adj[node] = []

    def add_edge(self, source, target, cost=1):
        if source not in self.adj:
            self.add_node(source)
        if target not in self.adj:
            self.add_node(target)
        
        if (target, cost) not in self.adj[source]:
            self.adj[source].append((target, cost))
    
    def neighbors(self, node):
        if node in self.adj:
            return self.adj[node]
        else:
            return []
    
    def has_node(self, node):
        if node in self.adj: return True
        else: return False
    
    def nodes(self):
        return list(self.adj.keys())
            